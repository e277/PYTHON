class Car:
    def say_speed(self) -> None:
        # self.print_speed(self)
        print(f"I'm going kph")

    def accelerate(self, speed):
        self.speed += speed

    def decelerate(self, speed):
        self.speed -= speed


if __name__ == "__main__":
    car = Car()
    car.say_speed()
    car.accelerate(12)
    car.say_speed()