# my_list = ["asd", "A", "hello"]


# data = {"Peter": 21, "George": 18, "John": 45}
#
#
# print(sorted(data.items(), key= lambda kvp: kvp[1]))

# def sorting_cheeses(**kwargs):
#     sorted_cheeses = sorted(kwargs.items(), key= lambda kvp: (-len(kvp[1]), kvp[0]))
#
#     result = ""
#     for cheese_name, quantities in sorted_cheeses:
#         result += cheese_name + "\n"
#         for quantity in sorted(quantities, reverse=True):
#             result += str(quantity) + "\n"
#
#     return result


def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key= lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ""
    for cheese_name, quantities in sorted_cheeses:
        result += cheese_name + "\n"
        for quantity in sorted(quantities, reverse=True):
            result += str(quantity) + "\n"
    return result








print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )

