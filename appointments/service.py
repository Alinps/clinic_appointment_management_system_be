from datetime import datetime, timedelta

from doctors.models import (DoctorAvailability,DoctorLeave)
from dashboard.models import ClinicSettings
from .models import Appointment




def generate_slots(doctor, appointment_date):

    working_day = appointment_date.strftime("%A").upper() # finding the date of the for checking the availabity of the doctor on that day

    availability = DoctorAvailability.objects.filter(
        doctor=doctor, 
        working_day=working_day
        ).first() # find the availability of doctor
    
    print(availability)

    if availability is None:

        return ["doctor is not available on this day"] # return empty list if not available
    
    leave_exists = DoctorLeave.objects.filter( # find the available doctor has any leave on the appointment date
        doctor=doctor,
        start_leave_date__lte=appointment_date,
        end_leave_date__gte=appointment_date
    )

    if leave_exists:

        return ["doctor is on leave"] # return emply slot if leave exists
    
    settings = ClinicSettings.objects.first() 

    current = datetime.combine(
        appointment_date,
        availability.start_time
    ) # combining date with time for performing timedelta operation

    

    end = datetime.combine(
        appointment_date, 
        availability.end_time
    )
    print("current: ",current,"\nend: ",end)

    if end <= current:

        end += timedelta(days=1)


    slots = []

    while current < end:

        slot_end = current + timedelta(minutes=settings.slot_duration) # type: ignore

        slots.append({
            "start_time":current.time(), # building time slots
            "end_time":slot_end.time()
        })

        current = slot_end


    booked = Appointment.objects.filter(doctor=doctor, appointment_date=appointment_date) # finding booked appointments for removing the booked slots from the slots 


    booked_times = {
        appointment.appointment_time for appointment in booked # creating a set with booked time
    }

    available_slots = []

    for slot in slots: #

        if slot.get("start_time") not in booked_times:
            print(slot)
            available_slots.append(slot)

    return available_slots