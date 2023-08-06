import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import copy


def split_n(n, r):
    if not isinstance(n, int):
        raise TypeError(f"'n' must be integer; {type(n)} given.")
    if not all([isinstance(i, int) for i in r]):
        raise ValueError("Elements of 'r' must all be integer.")
    if sum(r) != 100:
        raise ValueError(f"Elements of 'r' must sum to 100; sum = {sum(r)}.")
    splits = []
    for i in r[:-1]:
        x = n * (i / 100)
        if x % 1 != 0:
            x = int(round(x, 0))
        else:
            x = int(x)
        splits.append(x)
    rem = n - sum(splits)
    if rem != 0:
        splits.append(rem)
    checksum = sum(splits)
    return splits if checksum == n else None


def lin_reg(X, Y):
    n = Y.shape[0]
    sum_X = np.sum(X)
    sum_Y = np.sum(Y)
    sum_XY = np.sum(X * Y)
    sum_Xsq = np.sum(X**2)
    numerator_w = (n * sum_XY) - (sum_X * sum_Y)
    numerator_b = (sum_Y * sum_Xsq) - (sum_X * sum_XY)
    denominator = (n * sum_Xsq) - (sum_X**2)
    w = numerator_w / denominator
    b = numerator_b / denominator
    return w, b


def make_data(
    X_range, n_samples, params=None, plot=False, fuzz=None, seed=None
):
    rng = np.random.default_rng(seed)

    if not isinstance(X_range, tuple):
        raise ValueError(
            f"Expected 2-tuple for 'X_range'; got {type(X_range)}."
        )
    if not all([isinstance(i, int) for i in X_range]):
        raise ValueError(f"'X_range' must be tuple of integers: (min, max).")
    if not isinstance(n_samples, int):
        raise ValueError(
            f"Expected integer for 'n_samples'; got {type(n_samples)}."
        )
    if fuzz:
        if not isinstance(fuzz, int) or (not 0 <= fuzz <= 3):
            raise ValueError(f"'fuzz' must be integer in [0,3].")
    if params:
        if not isinstance(params, tuple):
            raise ValueError(
                f"Expected 5-tuple for 'params'; got {type(params)}."
            )
        if len(params) != 5:
            raise ValueError(
                f"Expected 5-tuple for 'params'; got {len(params)}-tuple."
            )

        a, b, c, d, e = params

    else:
        mu = np.percentile(X_range, 25)
        std = mu * 0.5

        a = np.round(rng.normal(mu, std), 3)
        b = np.round(rng.integers(np.floor(X_range[1])) + rng.random(), 3)
        c = np.round(rng.integers(np.floor(X_range[1])) + rng.random(), 3)
        d = np.round(rng.integers(np.floor(X_range[1])) + rng.random(), 3)
        e = np.round(rng.uniform(-2, 2), 3)

    X = np.linspace(X_range[0], X_range[1], n_samples)

    cos_val = np.cos(2 * np.pi * X / b - c)
    Y = a * cos_val + d + e * X

    if fuzz == 1:
        Y_fuzzy = add_fuzz(Y, 1, 0, X_range[1] * 0.01, seed=seed)

    elif fuzz == 2:
        Y_fuzzy = add_fuzz(Y, 1, 0, X_range[1] * 0.01, seed=seed)
        Y_fuzzy = add_fuzz(Y_fuzzy, 0.3, 0, X_range[1] * 0.075, seed=seed)

    elif fuzz == 3:
        Y_fuzzy = add_fuzz(Y, 1, 0, X_range[1] * 0.01, seed=seed)
        Y_fuzzy = add_fuzz(Y_fuzzy, 0.3, 0, X_range[1] * 0.075, seed=seed)
        Y_fuzzy = add_fuzz(Y_fuzzy, 0.05, 0, X_range[1] * 0.3, seed=seed)

    else:
        Y_fuzzy = Y

    if plot:
        plt.figure(figsize=(12, 4))
        plt.scatter(X, Y_fuzzy, color="teal", s=20, alpha=0.5)
        plt.plot(
            X,
            Y,
            color="mediumturquoise",
            alpha=0.7,
            linewidth=7,
            solid_capstyle="round",
        )
        plt.show()

    return a, b, c, d, e, X, Y_fuzzy


def add_fuzz(Y, fraction, error_mu, error_std, seed=None):
    rng = np.random.default_rng(seed)

    error_n = int(Y.shape[0] * fraction)
    error_idxs = rng.choice(Y.shape[0], error_n, replace=False)

    errors = rng.normal(error_mu, error_std, error_n)

    Y_fuzzy = np.array(Y)
    Y_fuzzy[error_idxs] += errors

    return Y_fuzzy


def min_max_scale(i, a, b, data_min, data_max):
    scaled_i = (b - a) * (i - data_min) / (data_max - data_min) + a
    return scaled_i


def calculate_loss(Y, Y_pred):
    n = Y.shape[0]

    sq_errors = [(i[0] - i[1]) ** 2 for i in np.dstack((Y, Y_pred))[0]]
    mse = np.sum(sq_errors) / n

    return mse


def calculate_r2(Y, Y_pred):
    n = Y.shape[0]
    Y_mu = np.mean(Y)

    sq_errors = [(i[0] - i[1]) ** 2 for i in np.dstack((Y, Y_pred))[0]]
    sse = np.sum(sq_errors)

    sq_totals = [(i - Y_mu) ** 2 for i in Y]
    sst = sum(sq_totals)

    r2 = 1 - sse / sst

    return r2


def pred_plot(model, X_data, Y_data, test_data=None, dots=True):
    Y_pred = model.predict(X_data)
    mse = np.round(calculate_loss(Y_data, Y_pred), 4)
    r2 = np.round(calculate_r2(Y_data, Y_pred), 4)

    X_space = np.linspace(X_data[0], X_data[-1], 300)
    Y_predspace = model.predict(X_space)

    plt.figure(figsize=(12, 4))

    plt.plot(
        X_space,
        Y_predspace,
        color="tomato",
        linewidth=4,
        alpha=0.7,
        solid_capstyle="round",
    )

    if test_data is None:
        if dots:
            plt.scatter(X_data, Y_data, color="teal", alpha=0.5, s=20)

        else:
            plt.plot(X_data, Y_data, color="teal", solid_capstyle="round")

        plt.title(f"Loss = {mse}; R2 = {r2}")

    else:
        XY_train_recombined = np.dstack((X_data, Y_data))[0]

        XY_recombined = np.vstack((XY_train_recombined, test_data))
        XY_recombined = XY_recombined[np.argsort(XY_recombined[:, 0])]

        if dots:
            plt.scatter(
                XY_recombined[:, 0],
                XY_recombined[:, 1],
                color="teal",
                s=20,
                alpha=0.5,
            )

        else:
            plt.plot(
                XY_recombined[:, 0],
                XY_recombined[:, 1],
                color="teal",
                solid_capstyle="round",
                zorder=-1,
            )

        # plot test data with big dots
        plt.scatter(
            test_data[:, 0],
            test_data[:, 1],
            color="mediumturquoise",
            s=30,
            edgecolors="teal",
        )

        Y_pred_test = model.predict(test_data[:, 0])
        test_mse = np.round(calculate_loss(test_data[:, 1], Y_pred_test), 4)
        test_r2 = np.round(calculate_r2(test_data[:, 1], Y_pred_test), 4)

        plt.title(
            f"Train Loss = {mse}; Train R2 = {r2}\nTest Loss = {test_mse}; Test R2 = {test_r2}"
        )

    plt.grid(visible=True)
    plt.show()


def simple_plot(X_data, Y_data, test_data=None):
    fig, ax = plt.subplots(figsize=(12, 4))

    ax.scatter(X_data, Y_data, color="teal", alpha=0.5, s=20)

    if test_data is not None:
        # plot test data with big dots
        ax.scatter(
            test_data[:, 0],
            test_data[:, 1],
            color="mediumturquoise",
            s=30,
            edgecolors="teal",
        )

    ax.grid(visible=True)
    ax.set_axisbelow(True)
    plt.show()


class TrigModel:
    def __init__(self, initial_params=None, initializer=None, seed=None):
        if initial_params is None:
            initial_params = {
                "a": {"value": None, "trainable": True},
                "b": {"value": None, "trainable": True},
                "c": {"value": None, "trainable": True},
                "d": {"value": None, "trainable": True},
                "e": {"value": None, "trainable": True},
            }

        init_rng = np.random.default_rng(seed)

        if initializer is not None:
            random_init = initializer
        else:
            random_init = init_rng.uniform(-1, 1, size=5)

        for i, (k, v) in enumerate(initial_params.items()):
            if v["value"] is None:
                v["value"] = random_init[i]

        self.initial_params = copy.deepcopy(initial_params)
        self.params = copy.deepcopy(initial_params)
        self.training_history = None

    def predict(self, x):
        a = self.params["a"]["value"]
        b = self.params["b"]["value"]
        c = self.params["c"]["value"]
        d = self.params["d"]["value"]
        e = self.params["e"]["value"]

        cos_val = np.cos(2 * np.pi * x / b - c)
        pred = a * cos_val + d + e * x

        return pred

    def dL_da(self, X, Y):
        a = self.params["a"]["value"]
        b = self.params["b"]["value"]
        c = self.params["c"]["value"]
        d = self.params["d"]["value"]
        e = self.params["e"]["value"]
        n = X.shape[0]

        cos_val = np.cos(2 * np.pi * X / b - c)
        dL_da = (1 / n) * np.sum(2 * cos_val * (a * cos_val + d + e * X - Y))
        return dL_da

    def dL_db(self, X, Y):
        a = self.params["a"]["value"]
        b = self.params["b"]["value"]
        c = self.params["c"]["value"]
        d = self.params["d"]["value"]
        e = self.params["e"]["value"]
        n = X.shape[0]

        cos_val = np.cos(2 * np.pi * X / b - c)
        sin_val = np.sin(2 * np.pi * X / b - c)
        dL_db = (1 / n) * np.sum(
            (4 * np.pi * a * X * (a * cos_val + d + e * X - Y) * sin_val)
            / b**2
        )
        return dL_db

    def dL_dc(self, X, Y):
        a = self.params["a"]["value"]
        b = self.params["b"]["value"]
        c = self.params["c"]["value"]
        d = self.params["d"]["value"]
        e = self.params["e"]["value"]
        n = X.shape[0]

        cos_val = np.cos(2 * np.pi * X / b - c)
        sin_val = np.sin(2 * np.pi * X / b - c)
        dL_dc = (1 / n) * np.sum(
            2 * (a * cos_val + d + e * X - Y) * (a * sin_val)
        )
        return dL_dc

    def dL_dd(self, X, Y):
        a = self.params["a"]["value"]
        b = self.params["b"]["value"]
        c = self.params["c"]["value"]
        d = self.params["d"]["value"]
        e = self.params["e"]["value"]
        n = X.shape[0]

        cos_val = np.cos(2 * np.pi * X / b - c)
        dL_dd = (1 / n) * np.sum(2 * (a * cos_val + d + e * X - Y))
        return dL_dd

    def dL_de(self, X, Y):
        a = self.params["a"]["value"]
        b = self.params["b"]["value"]
        c = self.params["c"]["value"]
        d = self.params["d"]["value"]
        e = self.params["e"]["value"]
        n = X.shape[0]

        cos_val = np.cos(2 * np.pi * X / b - c)
        dL_de = (1 / n) * np.sum(2 * X * (a * cos_val + d + e * X - Y))
        return dL_de

    def compile_diff_funcs(self):
        diff_funcs = [
            ("a", self.dL_da),
            ("b", self.dL_db),
            ("c", self.dL_dc),
            ("d", self.dL_dd),
            ("e", self.dL_de),
        ]

        trainable_params = {
            k: v["value"]
            for k, v in self.params.items()
            if self.params[k]["trainable"]
        }
        diff_funcs = [f for f in diff_funcs if f[0] in trainable_params.keys()]

        return diff_funcs

    def fit(
        self, X, Y, epochs=5, learning_rate=0.1, momentum=None, save_best=False
    ):
        Y_pred = self.predict(X)
        mse = calculate_loss(Y_pred, Y)
        r2 = calculate_r2(Y, Y_pred)

        training_history = np.array(
            [
                mse,
                r2,
                self.params["a"]["value"],
                self.params["b"]["value"],
                self.params["c"]["value"],
                self.params["d"]["value"],
                self.params["e"]["value"],
            ]
        )

        if self.training_history is None:
            self.training_history = training_history

        print(f"Initial Loss: {mse}")

        self.diff_funcs = self.compile_diff_funcs()
        if momentum:
            v = np.zeros(len(self.diff_funcs))

        for epoch in tqdm(range(1, epochs + 1)):
            res = np.array(training_history)

            for i, f in enumerate(self.diff_funcs):
                param_name = f[0]
                p = self.__dict__["params"][param_name]["value"]

                dL_dp = f[1]
                dp = dL_dp(X, Y)

                if momentum:
                    v[i] = momentum * v[i] - learning_rate * dp
                    p = p + v[i]
                else:
                    p = p - learning_rate * dp

                self.__dict__["params"][param_name]["value"] = p

                res[i + 2] = p

            Y_pred = self.predict(X)

            mse = calculate_loss(Y_pred, Y)
            res[0] = mse

            r2 = calculate_r2(Y, Y_pred)
            res[1] = r2

            self.training_history = np.vstack((self.training_history, res))

        print(f"Final Loss: {mse}")

        self.best_epoch = self.training_history.argmin(axis=0)[0]

        self.best_params = self.training_history[self.best_epoch][2:]

        if save_best:
            self.params["a"]["value"] = self.best_params[0]
            self.params["b"]["value"] = self.best_params[1]
            self.params["c"]["value"] = self.best_params[2]
            self.params["d"]["value"] = self.best_params[3]
            self.params["e"]["value"] = self.best_params[4]

    def loss_vis(self, param_name, markers=False):
        if self.training_history is None:
            raise ValueError(
                "No training history - model has not yet been fit."
            )

        if self.params[param_name]["trainable"]:
            col = "abcde".find(param_name) + 2

            p_values = self.training_history[:, col]
            loss_values = self.training_history[:, 0]

            fig, ax = plt.subplots(figsize=(12, 4))

            ax.scatter(
                p_values[0],
                loss_values[0],
                color="white",
                edgecolors="royalblue",
                s=60,
            )
            if markers:
                ax.plot(
                    p_values,
                    loss_values,
                    color="royalblue",
                    zorder=-1,
                    marker="o",
                )
            else:
                ax.plot(p_values, loss_values, color="royalblue", zorder=-1)
            ax.scatter(p_values[-1], loss_values[-1], color="black", s=60)
            plt.show()

        else:
            raise ValueError(f"{param_name} is not a trainable parameter.")

    def plot_training(self, metric):
        best_loss = self.training_history[self.best_epoch][0]
        best_r2 = self.training_history[self.best_epoch][1]
        epochs = range(self.training_history.shape[0])
        titles = ["Loss", "R-Squared"]

        if (metric == "loss") or (metric == "r2"):
            if metric == "loss":
                plot_data = self.training_history[:, 0]
                title = titles[0]
                best = self.training_history[self.best_epoch][0]
                color = "royalblue"
            else:
                plot_data = self.training_history[:, 0]
                title = titles[1]
                best = self.training_history[self.best_epoch][1]
                color = "crimson"

            plt.figure(figsize=(7, 4))
            plt.plot(
                epochs,
                plot_data,
                linewidth=4,
                alpha=0.8,
                solid_capstyle="round",
                color=color,
                zorder=-1,
            )

            plt.scatter(
                self.best_epoch, best, color="white", edgecolors=color, s=60
            )
            plt.title(title)
            plt.grid(visible=True)
            plt.show()

        elif metric == "both":
            best = [best_loss, best_r2]
            color = ["royalblue", "crimson"]

            fig, axs = plt.subplots(1, 2, figsize=(12, 4))
            for i in range(2):
                axs[i].plot(
                    epochs,
                    self.training_history[:, i],
                    linewidth=4,
                    alpha=0.8,
                    solid_capstyle="round",
                    color=color[i],
                    zorder=-1,
                )
                axs[i].scatter(
                    self.best_epoch,
                    best[i],
                    color="white",
                    edgecolors=color[i],
                    s=60,
                )
                axs[i].set_xlabel("Epochs")
                axs[i].set_title(titles[i])
                axs[i].grid(visible=True)
            plt.show()

        else:
            raise ValueError(f"Unkown metric: {metric}.")


def single_param_loss_vis(
    param_name,
    param_space,
    initial_params,
    X,
    Y,
    learning_rate=0.1,
    epochs=5,
    momentum=None,
    random_init=False,
    plot_all=False,
    seed=None,
):
    """
    Performs gradient descent on single parameter (keeping other parameters
    constant), and plots the parameter updates.

    Args:
    -----

        param_name (str): the chosen parameter to on which to perform gradient
        descent. Must be one of "a", "b", "c", "d", or "e".

        param_space (1-D array): value space for the chosen parameter.

        initial_params (dict): initial values for each of the parameters "a",
        "b", "c", "d", and "e" (dict keys). Note that only the chosen parameter
        will be updated; the others will be held constant.

        X (1-D array): input training data (features).

        Y (1-D array): output training data (values).

    Kwargs:
    -------

        learning_rate (float, default = 0.1): constant multiple for calculating
        parameter update step in each epoch, where:
            new param value = old param value - learning_rate * deriv

        epochs (int, default = 5): number of times to process entire dataset and
        update parameter values through gradient descent.

        momentum (float, default = None): if given, will apply gradient descent
        with momentum, taking into account prior gradients, where:
            new velocity = momentum * old velocity - learning_rate * deriv
            new param value = old param value + new velocity

        random_init (bool, default = False): if True, will initialize the chosen
        parameter value randomly. Otherwise, the initial value will be taken
        from the 'initial_params' arg.

        plot_all (bool, default = False): if True, will plot all of the parameter
        values computed during gradient descent.

        seed (int, default = None): sets random seed.

    Returns:
    --------

        Plot showing the parameter values computed through gradient descent,
        highlighting the initial and final values.
    """

    n = X.shape[0]
    params = copy.deepcopy(initial_params)

    if random_init:
        init_rng = np.random.default_rng(seed)
        initial_param_value = init_rng.choice(param_space)
    else:
        initial_param_value = initial_params[param_name]

    params[param_name] = initial_param_value

    def _fetch_params():
        a = params["a"]
        b = params["b"]
        c = params["c"]
        d = params["d"]
        e = params["e"]

        return a, b, c, d, e

    def _loss(a, b, c, d, e):
        cos_val = np.cos(2 * np.pi * X / b - c)
        Y_pred = a * cos_val + d + e * X
        sq_errors = [(i[0] - i[1]) ** 2 for i in np.dstack((Y, Y_pred))[0]]
        loss = np.sum(sq_errors) / n

        return loss

    def _get_loss_space(param_name, param_space):
        loss_space = []
        for i in param_space:
            a, b, c, d, e = _fetch_params()

            if param_name == "a":
                a = i
            elif param_name == "b":
                b = i
            elif param_name == "c":
                c = i
            elif param_name == "d":
                d = i
            elif param_name == "e":
                e = i

            loss = _loss(a, b, c, d, e)
            loss_space.append(loss)
        loss_space = np.array(loss_space)
        return loss_space

    def _get_deriv(param_name):
        a, b, c, d, e = _fetch_params()

        cos_val = np.cos(2 * np.pi * X / b - c)
        sin_val = np.sin(2 * np.pi * X / b - c)

        if param_name == "a":
            deriv = (1 / n) * np.sum(
                2 * cos_val * (a * cos_val + d + e * X - Y)
            )
        elif param_name == "b":
            deriv = (1 / n) * np.sum(
                (4 * np.pi * a * X * (a * cos_val + d + e * X - Y) * sin_val)
                / b**2
            )
        elif param_name == "c":
            deriv = (1 / n) * np.sum(
                2 * (a * cos_val + d + e * X - Y) * (a * sin_val)
            )
        elif param_name == "d":
            deriv = (1 / n) * np.sum(2 * (a * cos_val + d + e * X - Y))
        elif param_name == "e":
            deriv = (1 / n) * np.sum(2 * X * (a * cos_val + d + e * X - Y))
        else:
            deriv = 0

        return deriv

    p_values = [initial_param_value]
    a, b, c, d, e = _fetch_params()
    initial_loss = _loss(a, b, c, d, e)
    loss_values = [initial_loss]

    if momentum:
        v = 0

    for i in tqdm(range(1, epochs + 1)):
        deriv = _get_deriv(param_name)
        old_p = params[param_name]
        if momentum:
            v = momentum * v - learning_rate * deriv
            new_p = old_p + v
        else:
            new_p = old_p - learning_rate * deriv
        params[param_name] = new_p

        a, b, c, d, e = _fetch_params()
        loss = _loss(a, b, c, d, e)

        p_values.append(new_p)
        loss_values.append(loss)

    loss_space = _get_loss_space(param_name, param_space)
    param_combined = np.concatenate((param_space, p_values))
    loss_combined = np.concatenate((loss_space, loss_values))
    res_combined = np.dstack((param_combined, loss_combined))[0]
    res_combined = res_combined[np.argsort(res_combined[:, 0])]
    param_points = res_combined[:, 0]
    loss_points = res_combined[:, 1]

    fig, ax = plt.subplots(figsize=(12, 4))

    ax.set_xlim(left=np.min(param_points), right=np.max(param_points))

    y_buffer = (np.max(loss_points) - np.min(loss_points)) * 0.1
    ax.set_ylim(
        bottom=np.min(loss_points) - y_buffer,
        top=np.max(loss_points) + y_buffer,
    )

    # plot full parameter / loss space
    ax.plot(
        param_points,
        loss_points,
        color="tomato",
        linewidth=3,
        solid_capstyle="round",
        zorder=0,
    )

    # plot all parameter / loss values
    if plot_all:
        res_points = zip(p_values, loss_values)

        for i, j in enumerate(res_points):
            x_j = j[0]
            y_j = j[1]
            ax.scatter(x_j, y_j, color="teal", zorder=1, s=30)

    # plot lines marking minimum loss values
    ax.plot(
        (np.min(param_points), p_values[-1]),
        (loss_values[-1], loss_values[-1]),
        color="steelblue",
        alpha=0.7,
        linestyle="--",
        zorder=-1,
    )

    ax.plot(
        (p_values[-1], p_values[-1]),
        (np.min(loss_points) - y_buffer, loss_values[-1]),
        color="steelblue",
        alpha=0.7,
        linestyle="--",
        zorder=-1,
    )

    # plot initial and final parameter / loss value
    ax.scatter(
        initial_param_value,
        initial_loss,
        color="white",
        edgecolors="tomato",
        zorder=2,
        s=60,
    )
    ax.scatter(p_values[-1], loss_values[-1], color="black", zorder=2, s=60)

    plt.show()


def get_local_extrema(X, Y, span):
    XY = np.dstack((X, Y))[0]

    local_minima = []
    local_maxima = []

    for i, j in enumerate(XY):
        start_idx = np.max([0, i - span])
        end_idx = np.min([XY.shape[0] - 1, i + span])

        regional_min = XY[start_idx : end_idx + 1].min(axis=0)[1]
        if regional_min == j[1]:
            local_minima.append(j)

        regional_max = XY[start_idx : end_idx + 1].max(axis=0)[1]
        if regional_max == j[1]:
            local_maxima.append(j)

    local_minima = np.array(local_minima)
    local_maxima = np.array(local_maxima)

    return local_minima, local_maxima
