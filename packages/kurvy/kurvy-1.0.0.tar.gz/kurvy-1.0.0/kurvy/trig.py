import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import copy

from kurvy import utils


def make_data(X_range, n_samples, params=None, fuzz=None, seed=None):
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
        Y_fuzzy = utils.add_fuzz(Y, 1, 0, X_range[1] * 0.01, seed=seed)

    elif fuzz == 2:
        Y_fuzzy = utils.add_fuzz(Y, 1, 0, X_range[1] * 0.01, seed=seed)
        Y_fuzzy = utils.add_fuzz(Y_fuzzy, 0.3, 0, X_range[1] * 0.075, seed=seed)

    elif fuzz == 3:
        Y_fuzzy = utils.add_fuzz(Y, 1, 0, X_range[1] * 0.01, seed=seed)
        Y_fuzzy = utils.add_fuzz(Y_fuzzy, 0.3, 0, X_range[1] * 0.075, seed=seed)
        Y_fuzzy = utils.add_fuzz(Y_fuzzy, 0.05, 0, X_range[1] * 0.3, seed=seed)

    else:
        Y_fuzzy = Y

    return (a, b, c, d, e), X, Y_fuzzy


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
        mse = utils.calculate_loss(Y_pred, Y)
        r2 = utils.calculate_r2(Y, Y_pred)

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

            mse = utils.calculate_loss(Y_pred, Y)
            res[0] = mse

            r2 = utils.calculate_r2(Y, Y_pred)
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


#     def loss_vis(self, param_name, markers=False):
#         if self.training_history is None:
#             raise ValueError(
#                 "No training history - model has not yet been fit."
#             )

#         if self.params[param_name]["trainable"]:
#             col = "abcde".find(param_name) + 2

#             p_values = self.training_history[:, col]
#             loss_values = self.training_history[:, 0]

#             fig, ax = plt.subplots(figsize=(12, 4))

#             ax.scatter(
#                 p_values[0],
#                 loss_values[0],
#                 color="white",
#                 edgecolors="royalblue",
#                 s=60,
#             )
#             if markers:
#                 ax.plot(
#                     p_values,
#                     loss_values,
#                     color="royalblue",
#                     zorder=-1,
#                     marker="o",
#                 )
#             else:
#                 ax.plot(p_values, loss_values, color="royalblue", zorder=-1)
#             ax.scatter(p_values[-1], loss_values[-1], color="black", s=60)
#             plt.show()

#         else:
#             raise ValueError(f"{param_name} is not a trainable parameter.")

#     def plot_training(self, metric):
#         best_loss = self.training_history[self.best_epoch][0]
#         best_r2 = self.training_history[self.best_epoch][1]
#         epochs = range(self.training_history.shape[0])
#         titles = ["Loss", "R-Squared"]

#         if (metric == "loss") or (metric == "r2"):
#             if metric == "loss":
#                 plot_data = self.training_history[:, 0]
#                 title = titles[0]
#                 best = self.training_history[self.best_epoch][0]
#                 color = "royalblue"
#             else:
#                 plot_data = self.training_history[:, 0]
#                 title = titles[1]
#                 best = self.training_history[self.best_epoch][1]
#                 color = "crimson"

#             plt.figure(figsize=(7, 4))
#             plt.plot(
#                 epochs,
#                 plot_data,
#                 linewidth=4,
#                 alpha=0.8,
#                 solid_capstyle="round",
#                 color=color,
#                 zorder=-1,
#             )

#             plt.scatter(
#                 self.best_epoch, best, color="white", edgecolors=color, s=60
#             )
#             plt.title(title)
#             plt.grid(visible=True)
#             plt.show()

#         elif metric == "both":
#             best = [best_loss, best_r2]
#             color = ["royalblue", "crimson"]

#             fig, axs = plt.subplots(1, 2, figsize=(12, 4))
#             for i in range(2):
#                 axs[i].plot(
#                     epochs,
#                     self.training_history[:, i],
#                     linewidth=4,
#                     alpha=0.8,
#                     solid_capstyle="round",
#                     color=color[i],
#                     zorder=-1,
#                 )
#                 axs[i].scatter(
#                     self.best_epoch,
#                     best[i],
#                     color="white",
#                     edgecolors=color[i],
#                     s=60,
#                 )
#                 axs[i].set_xlabel("Epochs")
#                 axs[i].set_title(titles[i])
#                 axs[i].grid(visible=True)
#             plt.show()

#         else:
#             raise ValueError(f"Unkown metric: {metric}.")
