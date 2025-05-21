from glob import glob
import argparse, sys, os

def main():
    parser = argparse.ArgumentParser(prog='icon-desaturatorinator')
    parser.add_argument('theme_path')
    parser.add_argument('--amount', '-a', default=80, help='Amount to grayscale icons in percentage')

    parsed = parser.parse_args(sys.argv[1:])

    if not os.path.isdir(parsed.theme_path):
        print("Theme path is not a valid directory!")
        return

    if not os.access(parsed.theme_path, os.W_OK):
        print("Write privilages is limited, run this with sudo!")
        return

    for path in glob(parsed.theme_path + "/**/*.svg", recursive=True):
        contents = ""
        
        with open(path, "r") as file:
            contents = file.read()

        with open(path, "w") as file:
            if "filter: grayscale(" in contents:
                print("WARNING: ", path, " Already has grayscale filter, skipping..")
                continue

            file.write(contents.replace("</svg>", 
                                        "<style>"
                                        "svg {"
                                            "filter: grayscale("+str(parsed.amount)+"%);"
                                        "}"
                                        "</style>"
                                        "</svg>"))
        print("Edited: ", path)

if __name__ == '__main__':
    main()
