
#Module should contain all the related functions and classes
#helps in better organizing our codes

import converters

print(converters.kg_to_lbs(80))


from converters import lbs_to_kg
print(lbs_to_kg(90))

from datetime import time, timezone
print(timezone)