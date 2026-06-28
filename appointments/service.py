from datetime import datetime, timedelta

from doctors.models import (DoctorAvailability,DoctorLeave)
from dashboard.models import ClinicSettings
from .models import Appointment

from .utils.generate_slots import generate_slots_from_availability




def generate_slots(doctor, appointment_date):

    settings =ClinicSettings.objects.first()

    if settings is None:
        raise ValueError("Clinic settings not configured")

    slot_duration = settings.slot_duration # type: ignore

    working_day = appointment_date.strftime("%A").upper() # finding the date of the for checking the availabity of the doctor on that day
    
    previous_date = appointment_date - timedelta(days=1)

    previous_day = previous_date.strftime("%A").upper()

        
    
    leave_exists = DoctorLeave.objects.filter( # find the available doctor has any leave on the appointment date
        doctor=doctor,
        start_leave_date__lte=appointment_date,
        end_leave_date__gte=appointment_date
    ).exists()

    if leave_exists:

        return [] # return emply slot if leave exists
    
    slots = []
    
    # ----------------------------
    # Today's availability
    # ----------------------------

    today_availability = DoctorAvailability.objects.filter(
        doctor=doctor,
        working_day=working_day
    )
    

    if today_availability:

        for availability in today_availability:

            generated_slots = generate_slots_from_availability(
                availability,
                appointment_date,
                slot_duration
            )


            generated_slots = [
                slot
                for slot in generated_slots
                if slot["appointment_date"] == appointment_date
            ]

            slots.extend(generated_slots)


    #--------------------------------------
    # previous day's overnight availability
    #--------------------------------------


    previous_availability = DoctorAvailability.objects.filter(
        doctor=doctor,
        working_day=previous_day
    )

    if previous_availability:

        for availability in previous_availability:

            if (availability.end_time <= availability.start_time): 

                overnight_slots = generate_slots_from_availability(availability, previous_date, slot_duration)

                overnight_slots = [
                    slot 
                    for slot in overnight_slots 
                    if slot["appointment_date"] == appointment_date  #type: ignore
                ]
            
                slots.extend(overnight_slots)
    #--------------------------------------
    # Remove booked slots
    #--------------------------------------

    booked = Appointment.objects.filter(
        doctor=doctor,
        appointment_date=appointment_date
    )

    booked_times =  {
        appointment.appointment_time
        for appointment in booked
    }

    available_slots = [
        slot
        for slot in slots
        if slot["appointment_time"] not in booked_times
    ]


    available_slots.sort(key=lambda slot:slot["appointment_time"])

    if not available_slots:

        return []
    
    unique_slots = {}

    for slot in available_slots:
        key = (
            slot["appointment_date"],
            slot["appointment_time"]
        )
        unique_slots[key] = slot

    available_slots = list(unique_slots.values())
    
    return available_slots




   