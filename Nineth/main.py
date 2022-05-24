from means_of_transport import *


def main():
    lst = [
            Car("HM2131DG", "Avreliy", 3),
            Bus("LKJJHGF", "Antoniy", 51),
            Airplane("KGHDGHBLVB", "Zukerberg", 35),
            Trolley("KJSDGF", "Kuzevalov", 69),
            Tramway("LJHGHJGF", "Klavdiy", False)
          ]
    for i in lst:
        print(i)


if __name__ == "__main__":
    main()
