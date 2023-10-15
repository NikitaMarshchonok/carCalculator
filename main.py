import calculator

#thakyuykk
if __name__ == '__main__':
        calc = calculator.Calculator()
        calc.add_car(calculator.Car("Toyota Rav4", price=30000, fuel_economy=7, service_cost=1200, insurance_cost=2500))

        calc.add_car(calculator.Car("Mercedes-Benz", price=130000, fuel_economy=9, service_cost=2200, insurance_cost=3500))

        calc.add_car(calculator.Car("BMW", price=70000, fuel_economy=6, service_cost=1900, insurance_cost=2100))

        #calc.add_car(calculator.ElectricCar("Tesla model 3", 330000, 5000, 150))


calc.print_cars()