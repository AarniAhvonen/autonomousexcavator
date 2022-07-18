def interpolation(d, x, y):
    output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1]) / (d[1][0] - d[0][0]))
    # y = y1 + (x - x1) * ((y2 - y1) / (x2 - x1))
    if output > y[1]:
        output = y[1]
        return output
    elif output < y[0]:
        output = 0
        return output
    else:
        return output


if __name__ == "__main__":
    angle_list = []
    user_angle1 = angle_list.append(float(input("Enter angle for joint1: ")))
    user_angle2 = angle_list.append(float(input("Enter angle for joint2: ")))
    user_angle3 = angle_list.append(float(input("Enter angle for joint3: ")))

    # angle, amps
    joint1_angle = [[0, 0.0058], [-2.24414, 0.0169]]
    joint2_angle = [[0, 0.0039], [-1.93801, 0.0168]]
    joint3_angle = [[0, 0.00410], [-3.32415, 0.0139]]

    boom_min_max = [0.0058, 0.0169]
    stick_min_max = [0.0039, 0.0168]
    bucket_min_max = [0.00410, 0.0139]

    # Finding the interpolation

    boom_ma = interpolation(joint1_angle, angle_list[0], boom_min_max)
    stick_ma = interpolation(joint2_angle, angle_list[1], stick_min_max)
    bucket_ma = interpolation(joint3_angle, angle_list[2], bucket_min_max)

    print("Amps for the input angle in joint 1 is {:.5f}mA".format(boom_ma))
    print("Amps for the input angle in joint 2 is {:.5f}mA".format(stick_ma))
    print("Amps for the input angle in joint 3 is {:.5f}mA".format(bucket_ma))





    # joint1_length = [[0, 0.006], [325, 0.0164]]
    # joint2_length = [[0, 0.0039], [430, 0.0165]]
    # joint3_length = [[0, 0.00418], [292, 0.0134]]

    # user_length1 = float(input("Enter length for joint1: "))

    # user_angle2 = float(input("Enter angle for joint2: "))
    # user_length2 = float(input("Enter length for joint2: "))

    # user_angle3 = float(input("Enter angle for joint3: "))
    # user_length3 = float(input("Enter length for joint3: "))

    # print("Amps for the input angle and length in joint 2 is {:.4f}mA and {:.4f}mA".
    # format(interpolation(joint1_angle, user_angle2),
    # (interpolation(joint1_length, user_length2))))

    # print("Amps for the input angle and length in joint 3 is {:.4f}mA and {:.4f}mA".
    # format(interpolation(joint1_angle, user_angle3),
    # (interpolation(joint1_length, user_length3))))
