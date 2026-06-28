from datetime import datetime, timedelta

def generate_slots_from_availability(availability, base_date, slot_duration):
    
    current = datetime.combine(base_date, availability.start_time)
    end = datetime.combine(base_date, availability.end_time)

    # Overnight shift
    if end <= current:
        end += timedelta(days=1)

    slots = []

    while current + timedelta(minutes=slot_duration) <= end:
        slots.append({
            "appointment_date": current.date(),
            "appointment_time": current.time()
        })

        current += timedelta(minutes=slot_duration)

    return slots