cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeep_cars = ", "
    print(jeep_cars.join(cars['Jeep']))
    return jeep_cars.join(cars['Jeep'])
    pass


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_car = [cars[key][0] for key in cars]
    # for key in cars:
    #     first_car.append(cars[key][0])
    print(first_car)
    return first_car
    pass


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    carsMatching = [car for values in cars.values() for car in values if grep.upper() in car.upper()]
    # for values in cars.values():
    #     for car in values:
    #         if grep.upper() in car.upper():
    #             carsMatching.append(car)
    print(sorted(carsMatching))
    return sorted(carsMatching)
    pass


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    new_dict = {key : sorted(value) for key, value in cars.items()}
    # for key, value in cars.items():
    #     new_dict[key] = sorted(value)
    print(new_dict)
    return new_dict
    pass


get_all_jeeps()
get_first_model_each_manufacturer()
get_all_matching_models(grep="CO")
sort_car_models()