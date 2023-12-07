class PSD_Validator:
    def __init__(self):
        self.var_name_changed = []

    def validate_and_add(self, input_list):
        for item in input_list:
            if item.isdigit() and int(item) > 0:
                self.var_name_changed.append(int(item))
  
# Fixing the mistake. It's not you, it's me! MERRY CHRISTMAS and HAPPY NEW YEAR!!!
validator = PSD_Validator()
validator.validate_and_add(["1", "2", "three", "-4", "5"]) 
print(validator.var_name_changed)