import argparse


def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        formatted_lines = []
        for line in lines:
            formatted_line = ''
            line = line.strip()
            while len(line) > frame_width:
                formatted_line += line[:frame_width] + '\n'
                line = line[frame_width:]

            formatted_line += line
            formatted_lines.append(formatted_line)

        if len(formatted_lines) > frame_height:
            formatted_lines = formatted_lines[:frame_height]

        return '\n'.join(formatted_lines)

    except Exception as e:
        return str(e)


def main():
    parser = argparse.ArgumentParser(description='Format text file and display its content within specified frame')
    parser.add_argument('--frame-height', type=int, help='height of the frame in characters')
    parser.add_argument('--frame-width', type=int, help='width of the frame in characters')
    parser.add_argument('file_name', type=str, help='name of the input file')
    args = parser.parse_args()

    formatted_text = format_text_block(args.frame_height, args.frame_width, args.file_name)
    print(formatted_text)


if __name__ == '__main__':
    main()
