# delta
Delta is a lib for writing privacy computing task executed on [delta framework](https://deltampc.com/), uses Pytorch as it backend.
It helps users focus on implementing computing models and logic, no need to worry about the data privacy (Delta framework do it for you).

## install

First install pytorch

using pip:

```bash
pip install -U delta-task
```

install from source code:

git clone this repo

```bash
pip install .
```

## example

[example.py](example.py)

## usage

Now lib delta supports horizontal federated learning task.

## how to write a Task

In delta, you can define a horizontal federated learning task by inherit the base class `delta.task.HorizontalTask`

`HorizontalTask` is a abstract class, inspite of the constructor `__init__`, you have to implement the following four methods:

* train(self, dataloader: Iterable)
* get_params(self) -> List[torch.Tensor]
* validate(self, dataloader: Iterable) -> Dict[str, float]
* preprocess(self, x, y=None)

### __init__

```python
def __init__(self, name: str, dataset: str, max_rounds: int, validate_interval: int = 1, validate_frac: float = 0.1):
```

When inherit `HorizontalTask`, you must call the constructor of base class by `super().__init__`

params:

| param | type | description |
| - | - | - |
| name | string | the task name |
| dataset | string | the dataset which the task uses |
| max_rounds | int | max execution rounds of task |
| validate_interval | int | validation every {validate_interval} rounds |
| validate_frac | float | validation dataset percentage, should be in [0, 1) |

### train

```python
def train(self, dataloader: Iterable)
```

You can implement model training logic in this function, a traditional implementation is like this:

```python
def train(self, dataloader: Iterable):
    x, y = batch
    # forwarding
    y_pred = self.model(x)
    # loss calculation
    loss = self.loss_func(y_pred, y)
    # backwarding
    self.optimizer.zero_grad()
    loss.backward()
    self.optimizer.step()

```

params:

| param | type | description |
| - | - | - |
| dataloader | Iterable | the dataloader of training dataset |

### get_params

```python
def get_params(self) -> List[torch.Tensor]
```

Get trainable model parameters. Delta framework will secure aggregate theses parameters from different nodes to get the global model parameters.

A traditional implementation is like this:

```python
def get_params(self) -> List[torch.Tensor]:
    return list(self.model.parameters())
```

returns:

| type | description |
| - | - |
| List[torch.Tensor] | parameters list |

### validate

```python
def validate(self, dataloader: Iterable) -> Dict[str, float]
```

You can implement the validation logic in this function.
The validation result is a `Dict[str, float]`, whose key is the validation metric name, value is the vaidation metric value.
Delta framework will secure aggregate nodes' validation result to get the global validation result.

A traditional implementation is like this:

```python
def validate(self, dataloader: Iterable) -> Dict[str, float]:
    total_loss = 0
    count = 0
    ys = []
    y_s = []
    for batch in dataloader:
        x, y = batch
        y_pred = self.model(x)
        loss = self.loss_func(y_pred, y)
        total_loss += loss.item()
        count += 1

        y_ = torch.argmax(y_pred, dim=1)
        y_s.extend(y_.tolist())
        ys.extend(y.tolist())
    avg_loss = total_loss / count
    tp = len([1 for i in range(len(ys)) if ys[i] == y_s[i]])
    precision = tp / len(ys)

    return {"loss": avg_loss, "precision": precision}
```

In the above code, `validate` function compute the average loss and precision on the input validation dataset.

params:

| param | type | description |
| - | - | - |
| dataloader | Iterable | the dataloader of validation dataset |


### preprocess

```python
def preprocess(self, x, y=None)
```

Preprocess function preprocess each data item before training and validation.

The input parameter `x` is the data item, `y` is the corresponding data label if the dataset has a label.

The type of `x` depends on the dataset. It can be a `np.ndarray`, a `torch.Tensor`, a `pd.DataFrame` or a `Image.Image`.
In the preprocess function, you should convert the `x` to a `torch.Tensor`.

The type of `y` is string (if has `y`), means the label name, and you should convert it to a `torch.Tensor` compatible with your loss function.

The preprocess function should return two `torch.Tensor` if `x` and `y` all exist, or only return one `torch.Tensor`.


### (optional) dataloader_config

```python
def dataloader_config(self) -> Union[Dict[str, Any], Tuple[Dict[str, Any], Dict[str, Any]]]:
```

You can specify dataloader arguments in this function.

This function can return one or two dictionary as the kwargs passed to dataloader constructor.
If it returns only one dictionary, then the result will be passed to both training dataloader and validation dataloader.
If it returns two dictionary, then the first one will be passed to training dataloader, the second one will be passed to validation dataloader.

The default implementation is as the follows:

```python
def dataloader_config(
    self,
) -> Union[Dict[str, Any], Tuple[Dict[str, Any], Dict[str, Any]]]:
    return {"shuffle": True, "batch_size": 64, "drop_last": True}

```

### (optional) algorithm

```python
def algorithm(self) -> HorizontalAlgorithm:
```

You can specify secure aggregation algorithm in this function.

The algorithm you can use now is `delta.algorithm.horizontal.FedAvg` and `delta.algorithm.horizontal.FaultTolerantFedAvg`, which are subclasses of `delta.algorithm.horizontal.HorizontalAlgorithm`.

The difference between `FedAvg` and `FaultTolerantFedAvg` is that `FaultTolerantFedAvg` can tolerant some nodes being offline during secure aggregation, but `FedAvg` can't.

Parameters of `FedAvg` and `FaultTolerantFedAvg` are the same.

params:

| param | type | description |
| - | - | - |
| merge_interval_iter | int | aggregate every {merge_interval_iter} iter |
| merge_interval_epoch | int | aggregate every {merge_interval_epoch} round. This param is mutually exclusive with merge_interval_iter, only one of them can be greater than 0 |
| min_clients | int | minimal node count in a round |
| max_clients | int | maximal node count in a round |
| wait_timeout | Optional[float] | timeout in seconds for task computation in a round, default value is 60 second |
| connection_timeout | Optional[float] | timeout in seconds for each stage of the secure aggregation, default value is 60 second |
| precision | int | precision of the result. result will be rounded by this precision |
| curve | CURVE_TYPE | elliptic curve used for asymmetric encryption in the secure aggregation, default value is "secp256k1" |


## dataset format

Delta framework now supports four kinds of dataset format:

1. Numpy array, with file extension `.npy`, `.npz`
2. Torch tensor, with file extension `.pt`
3. Table file, with file extension `.csv`, `.tsv`, `.xls`, `.xlsx`. Table file will be loaded by `pandas`
4. Image file. Image file will be loaded by `PIL`

A dataset can be a single file or a directory. When creating a task, you can refer the dataset by its name.

When dataset is a single file, the first dimension of the data is the data sample, and each data sample has no label.

When dataset is a directory, there are two acceptable directory structure. 
The first one is that data files are placed in the directory. Each file represents a data sample and each data sample has no label.
The second one is that directory contains several sub directories, and each sub directory represents a class of data. The sub directory name is the class name.
Data files are placed in one sub directory according to its class.
