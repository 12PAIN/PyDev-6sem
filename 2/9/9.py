

def format_text_block(frame_height, frame_width, file_name):

    file = open(file_name, "r")
    text = file.read()
    file.close()

    newText = []
    globalLinesCursor = 0

    lines = text.split("\n")


    for line in lines:

        symWritten = 0
        heightCursor = 0
        lineCursor = 0

        while symWritten != len(line):




            currentLineText = line[lineCursor:widthCursor]

            newText.insert(globalLinesCursor+heightCursor, currentLineText)

            lineCursor = widthCursor

