from datetime import datetime

class TravelPackage:
    def __init__(self, start_date, end_date, destination, price):
        self.start_date = start_date
        self.end_date = end_date
        self.destination = destination
        self.price = price

    def display_details(self):
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Destination: {self.destination}")
        print(f"Price: ${self.price}")


class TravelPackageManager:
    def __init__(self):
        self.packages = []

    def add_package(self, package: object):
        self.packages.append(package)
        print("Travel package added successfully!")

    def display_all_packages(self):
        if not self.packages:
            print("There are no travel packages yet.")
        else:
            for index, package in enumerate(self.packages):
                print(f"Package {index + 1}:")
                assert isinstance(package.display_details, object)
                package.display_details()
                print()

    def add_package_manually(self):
        start_date, end_date, destination, price = input(
            "Enter package details (start_date, end_date, destination, price): ").strip().split(',')
        # 2025 12 5, 2025 12 10, Londra, 100
        package = TravelPackage(start_date, end_date, destination, float(price))
        self.add_package(package)

    def update_date(self, start_or_end, package_number):
        new_date = input("Please enter new date")
        package = self.packages[package_number - 1]
        if start_or_end == "start":
            package.start_date = new_date
        elif start_or_end == "end":
            package.end_date = new_date
            print(f"{start_or_end.capitalize()} updated succesfully")

    def update_destination(self, update_destination, package_number):
        new_destination = input("Please enter a new destination")
        package = self.packages[package_number - 1]
        package.destination = new_destination
        print(f"{update_destination.capitalize()} updated succesfully")

    def update_price(self, update_price, package_number):
        new_price = float(input("Please enter a new price"))
        package = self.packages[package_number - 1]
        package.price = new_price
        print(f"{update_price.capitalize()} updated succesfully")

    def modify_package(self):
        if not self.packages:
            print("Thare are no travel packages to be modified. ")
            return

        number = int(input("Which package do you want to modify? "))

        if number < 1 or number > len(self.packages):
            print("Invalid package number.")
            return

        while True:
            print("\n1. Start Date")
            print("2. End Date")
            print("3. Destination")
            print("4. Price")
            print("5. Exit")

            value = int(input("What do you want to modify? "))

            if value == 5:
                print("Exiting modification menu.")
                break

            options = {
                1: ("start", self.update_date),
                2: ("end", self.update_date),
                3: ("destination", self.update_destination),
                4: ("price", self.update_price)
            }
            attribute, update_method = options.get(value)
            if update_method:
                update_method(attribute, number)
            else:
                print("Invalid choice. Please enter a valid option")

    def load_packages_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    start_date, end_date, destination, price = line.strip().split(',')
                    destination = destination[1:]
                    package = TravelPackage(start_date, end_date, destination, float(price))
                    self.add_package(package)
        except FileNotFoundError:
            print(f"File '{file_name}' not fount.")
        except Exception as e:
            print(f"An error occurred while loading packages: {str(e)}")

    def delete_destination(self):
        destination_to_delete = input("Enter the destination you want to delete: ").strip()

        # we use a list comprehension to create a new list without the packages with the specified destination
        self.packages = [package for package in self.packages if package.destination != destination_to_delete]

        print(f"All packages with destination '{destination_to_delete}' have been deleted.")

    def number_of_days_between_dates(self, date_str1, date_str2):
        formats_to_try = ["%Y %m %d", "%Y %m%d", "%Y%m %d", "%Y%m%d"]

        for date_format in formats_to_try:
            try:
                date1 = datetime.strptime(date_str1.strip(), date_format)
                date2 = datetime.strptime(date_str2.strip(), date_format)
                delta = date2 - date1
                return delta.days
            except ValueError:
                pass

        raise ValueError(f"Unable to parse dates: {date_str1}, {date_str2} with any of the supported formats.")

    def del_number_days(self,days):
        packagess = [package for package in self.packages
                         if self.number_of_days_between_dates(package.start_date,package.end_date) >= days]
        return packagess

    def delete_package_number_of_days(self):
        try:
            number_of_days = int(input("Enter the minimum number of days a package should last"))

            if not self.packages:
                print("There are no travel packages to delete.")
                return

            self.packages = [package for package in self.packages
                             if
                             self.number_of_days_between_dates(package.start_date, package.end_date) >= number_of_days]

            print(f"Packages that aren't longer than {number_of_days} days were deleted.")
        except ValueError as ve:
            print(f"Error: {ve}. Please enter a valid integer for the number of days.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def interactive_menu(self):
        options = {
            1: self.add_package_manually,
            2: lambda: self.load_packages_from_file("travel_packages.txt"),
            3: self.display_all_packages,
            4: self.modify_package,
            5: self.delete_destination,
            6: self.delete_package_number_of_days,
            7: exit
        }
        while True:
            print("\nOptions:")
            print("1. Add a package manually")
            print("2. Load packages from a file")
            print("3. Display all packages")
            print("4. Modify package")
            print("5. Delete package for a certain destination")
            print("6. Delete package if it doesn't last longer than a number o days")
            print("7. Exit\n")

            choice = int(input("Enter your choice: "))

            selected_option = options.get(choice)
            if selected_option:
                if selected_option == exit:
                    print("Goodbye!")
                    break
                selected_option()
            else:
                print("Invalid choice. Please enter a valid option.")


# Example usage
if __name__ == "__main__":
    manager = TravelPackageManager()
    manager.interactive_menu()

# modul pt main/functii UI/functii operatii/aplicatie
# teste
# modul pt main/UI/operatii/domeniu - unde sunt definite structurile de date din program
