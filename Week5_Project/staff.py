class Mcdonald():
   def schedule_staff(self, shift_time):
        shift_time = 8
        staff_availability=[1,2,3,4,5,6,7]
        # Staff scheduling using binary search
        staff_availability = self.inventory['staff_availability']
        # Binary search to find available staff during the given shift time
        left, right = 0, len(staff_availability) - 1
        while left <= right:
            mid = (left + right) // 2
            if staff_availability[mid] == shift_time:
                return f"Staff available for shift at {shift_time} hours."
            elif staff_availability[mid] < shift_time:
                left = mid + 1
            else:
                right = mid - 1
        if staff_availability not in shift_time:
            print ("Staff is not available")
        else:
           return f"No available staff for shift at {shift_time} hours."