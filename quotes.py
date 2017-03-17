# python 3

def read_text(file):
    with open(file, 'r') as fin:
        return fin.read()


def main():
    transcript = "transcript.txt"
    text = read_text(transcript)
    print(text)


if __name__ == '__main__':
    main()
