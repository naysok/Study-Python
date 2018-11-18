if TF:
    now = "; Export Time - " + str(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    comment.append(now)
    comment.append("\n")

    height = "; Layer Height(mm) - " + str(layer_height)
    comment.append(height)
    comment.append("\n")

    count = "; Layer Count - " + str(layer_count)
    comment.append(count)
    comment.append("\n")


    amp = "; Extrude Amp - " + str(extrude_amp)
    comment.append(amp)
    comment.append("\n")
    comment.append("\n")

    f = open(path_out, "w")
    f.writelines(comment)
    f.writelines(debug)
    f.close()