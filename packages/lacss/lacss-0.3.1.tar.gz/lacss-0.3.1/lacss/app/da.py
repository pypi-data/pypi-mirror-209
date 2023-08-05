import typing as tp

import flax.linen as nn
import jax
import jax.numpy as jnp


class Discriminator(nn.Module):

    conv_spec: tp.Sequence[int] = (256, 512, 512)

    @nn.compact
    def _compute(self, x):
        for ch in self.conv_spec:
            x = nn.Conv(ch, (3, 3))(x)

        x = nn.Conv(1, (1, 1))(x)

        return x

    def __call__(
        self,
        x: jnp.ndarray,
    ) -> jnp.ndarray:

        x_const = jax.lax.stop_gradient(x)

        y_disc = self._compute(x_const)
        y_da = self._compute(-x)

        return y_disc, y_da


# def da_loss():
