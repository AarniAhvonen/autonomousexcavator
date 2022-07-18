def amps_to_angle(minimum_angle, minimum_amps, maximum_angle, maximum_amps,current_amps):
    angles_difference = maximum_angle - minimum_angle
    amps_diference = maximum_amps - minimum_amps
    angle = minimum_angle + (current_amps - minimum_amps) * (angles_difference / amps_diference)
    if angle < maximum_angle:
        return maximum_angle
    elif angle > minimum_angle:
        return minimum_angle
    else:
        return angle



if __name__ == "__main__":
    user_amps_boom = float(input("Enter amps for boom: "))
    user_amps_stick = float(input("Enter amps for stick: "))
    user_amps_bucket = float(input("Enter amps for bucket: "))

    # angle, amps
    boom_minimum = [0, 0.006]
    boom_maximum = [-2.24414, 0.0164]
    stick_minimum = [0, 0.0039]
    stick_maximum = [-1.93801, 0.0168]
    bucket_minimum = [0, 0.00410]
    bucket_maximum = [-3.32415, 0.0139]

    output_angles = []
    # Finding the interpolation
    boom_angle = amps_to_angle(boom_minimum[0], boom_minimum[1], boom_maximum[0], boom_maximum[1], user_amps_boom)
    stick_angle = amps_to_angle(stick_minimum[0], stick_minimum[1], stick_maximum[0], stick_maximum[1], user_amps_stick)
    bucket_angle = amps_to_angle(bucket_minimum[0], bucket_minimum[1], bucket_maximum[0], bucket_maximum[1], user_amps_bucket)
    output_angles = [boom_angle, stick_angle, bucket_angle]

    print("Angle for the input amps in joint 1 is {:.5f}".format(boom_angle))
    print("Angle for the input amps in joint 2 is {:.5f}".format(stick_angle))
    print("Angle for the input amps in joint 3 is {:.5f}".format(bucket_angle))

