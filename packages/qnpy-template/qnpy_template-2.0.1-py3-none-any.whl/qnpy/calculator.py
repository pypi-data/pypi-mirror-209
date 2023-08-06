import math


class Speed:
    def __init__(self, tire_spec, gear_ratios, axle_ratio) -> None:
        self.tire_spec = tire_spec
        self.gear_ratios = gear_ratios
        self.axle_ratio = axle_ratio
        
        self.tire_diameter = self._tire_diameter()

    def _tire_diameter(self):
        return 2 * self.tire_spec[0] * self.tire_spec[1] / 100 + self.tire_spec[2] * 25.4
    
    def speed(self, rpm_range, mph = False):
        print(f"{len(self.gear_ratios)} gears: ratio {', '.join(map(str, self.gear_ratios))}, final drive axle ratio {self.axle_ratio}, tire spec {self.tire_spec[0]}/{self.tire_spec[1]} R{self.tire_spec[2]}, diameter {self.tire_diameter}mm")
        print(f'speed in {"mph" if mph else "km/h"}')
        wheel_perimeter = self.tire_diameter * math.pi
        for rpm in rpm_range:
            speed_in_km_per_hour = []
            for gear_ratio in self.gear_ratios:
                wheel_rpm = rpm / gear_ratio / self.axle_ratio
                distance_mm_per_minute = wheel_rpm * wheel_perimeter
                speed_in_km_per_hour.append(distance_mm_per_minute * 60 / 1000_000)

            ratio = 0.621371 if mph else 1
            print(', '.join([f'RPM@{rpm}'] + [str(round(speed * ratio)) for speed in speed_in_km_per_hour]))
    

    

speed = Speed((215, 40, 18), [3.63, 2.19, 1.54, 1.21, 1.0, 0.77], 4.1)
speed.speed(range(100, 1000, 100), True)
speed.speed(range(1000, 10000, 1000), True)
