from config import *
from code.work_with_json import *
from code.parsing import *

def main():
    print(get_cities(get_html(LINK_CITIES_INFORMATION)))


if __name__ == "__main__":
    main()
