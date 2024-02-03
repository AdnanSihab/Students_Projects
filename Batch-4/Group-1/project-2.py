def Development_board():
    print("Development Boards are printed circuit boards with a microcontroller/microprocessor mounted on them with a few other hardware components. Development boards are meant for System Designers to become acquainted with programming a processor onboard and also to develop and test projects effectively and efficiently")
    print("There are different kinds of development boards like Arduino, ESP32, Raspberry Pi, etc.")
    print("To start robotics, Arduino is the best development board. There are different kinds of Arduino models like Arduino UNO, Arduino Mega, Arduino Nano.")
    print("Search on Google to see the photo of different kinds of development boards")

def Sensor():
    print("A sensor is a device that produces an output signal for the purpose of sensing a physical phenomenon. In the broadest definition, a sensor is a device, module, machine, or subsystem that detects events or changes in its environment and sends the information to other electronics, frequently a computer processor")
    print("To build up a robot, a sensor is a must. There are different kinds of sensors like temperature sensor, pressure sensor, gas sensor, soil moisture sensor, etc.")

def Electronic_device():
    print("Electronic device is another important thing to build up a robot. There are different kinds of electronic devices like actuator, motor, Servo Motor, water pump, etc.")
    print("To build up a robot you have to learn about many things about electronic devices")

def Module():
    print("Module is another important thing to build up a robot. There are different kinds of wireless modules like Bluetooth module, Wi-Fi module, etc. Besides, to start a motor shield which is a module is very important.")
    print("So learn about different kinds of modules")

def Programming():
    print("To work a robot, a development board is a must, to work a development board programming is a must.")
    print("Programming refers to a technological process for telling a computer which tasks to perform to solve problems. You can think of programming as a collaboration between humans and computers, in which humans create instructions for a computer to follow (code) in a language computers can understand.")
    print("There are different kinds of programming languages like C, C++, Java, Python, etc.")
    print("If you are a beginner in robotics, learn about Arduino. To work with Arduino, start to learn the C programming language. Then learn about other programming languages")

def Extra_thing():
    print("To complete learning about robotics, you can participate in any Olympiad like BDRO, Science Fair, etc.")
    print("Besides, there are different kinds of Robotics books. You can learn from these books")

def main():
    print("Welcome to Learn About Robotics ")
    print("Robotics is the interdisciplinary study and practice of the design, construction, operation, and use of robots. Within mechanical engineering, robotics is the design and construction of the physical structures of robots, while in computer science, robotics focuses on robotic automation algorithms.")
    print("This app is about how to start robotics. To start Robotics, you have to know what is a development board, what is programming, what is an electronic device, what is a sensor, and other things.")
    print("Press 1 to learn about development board.\nPress 2 to learn about sensor.\nPress 3 to learn about electronic device.\nPress 4 to learn about module.\nPress 5 to learn about programming.\nPress 6 to learn about extra thing")
    
    user_choice = int(input("Press = "))
    if user_choice == 1:
        Development_board()
    elif user_choice == 2:
        Sensor()
    elif user_choice == 3:
        Electronic_device()
    elif user_choice == 4:
        Module()
    elif user_choice == 5:
        Programming()
    elif user_choice == 6:
        Extra_thing()
    else:
        print("Wrong number.")

if __name__ == "__main__":
    main()