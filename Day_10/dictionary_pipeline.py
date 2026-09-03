# Standard mutable set
set_x = {1, 2, 3}
set_x.add(4)        #  Works
set_x.remove(2)     #  Works
# set_x[0]  Raises TypeError (sets are unordered, no indexing)

# Frozen set (immutable)
frozen_x = frozenset([1, 2, 2, 3, 3, 4])
print(frozen_x)     #duplicates removed

# frozen_x.add(5)  Raises AttributeError: 'frozenset' object has no attribute 'add'

# Valid dictionary with immutable keys
model_config = {
    "model_name": "GPT4",
    1: "version_1",
    True: "active",
    (1, 2): "coordinates"
}

#  Invalid: using a list as a key
#invalid_dict = { [1, 2]: "oops" }
# Raises: TypeError: unhashable type: 'list'

hyperparameters = {
    "learning_rate": 0.01,
    "dropout_rate": 0.23,
    "optimizer": "adam"
}

print(hyperparameters["optimizer"])   #  "adam"
# print(hyperparameters["dropout"])   KeyError: 'dropout'

# Safe fetching
print(hyperparameters.get("dropout", "Key not found"))  # "Key not found"

# Duplicate key overwriting
hyperparameters["dropout_rate"] = 0.3
hyperparameters["dropout_rate"] = 0.6
print(hyperparameters["dropout_rate"])  #  0.6

pipeline_config = {
    "GPT4": {"layers": 48, "parameters": 175e9, "attention_heads": 96},
    "BERT": {"layers": 12, "parameters": 110e6, "attention_heads": 12},
    "Opus4": {"layers": 64, "parameters": 200e9, "attention_heads": 128}
}

print(pipeline_config["BERT"]["parameters"])  # 110000000.0
print(pipeline_config["GPT4"]["layers"])      #  48


model_params = {"epochs": 10, "batch_size": 32}

# Shared reference
shared_params = model_params
shared_params["epochs"] = 20
print(model_params["epochs"])  #  20 (same memory reference)

# Shallow copy
safe_params = model_params.copy()
model_params.clear()
print(model_params)   #  {}
print(safe_params)    #  {'epochs': 20, 'batch_size': 32}

# Merging
base_config = {"epochs": 5, "lr": 0.01}
version_config = {"epochs": 15, "optimizer": "adam"}
base_config.update(version_config)
print(base_config)    #  {'epochs': 15, 'lr': 0.01, 'optimizer': 'adam'}

config = {"batch_size": 32, "epochs": 10, "lr": 0.01}

print(config.keys())    # dict_keys([...])
print(config.values())  # dict_values([...])
print(config.items())   # dict_items([...])

# Tuple unpacking
for key, value in config.items():
    print(key, ":", value)

# Membership
if "batch_size" in config.keys():
    print("Key exists")
if 32 in config.values():
    print("Value exists")

# Set operations on keys
config_a = {"epochs": 10, "lr": 0.01}
config_b = {"epochs": 20, "optimizer": "adam"}

print(config_a.keys() & config_b.keys())  #  {'epochs'}
print(config_a.keys() | config_b.keys())  #  {'epochs', 'lr', 'optimizer'}

data = {"name": "Alex", "age": 25, "city": "Hyderabad"}

# Targeted removal
print(data.pop("age"))   #  25
# data.pop()  TypeError: pop expected at least 1 argument

# Last-item removal
print(data.popitem())    # ('city', 'Hyderabad')

# Full wipe
data.clear()
print(data)              #  {}
