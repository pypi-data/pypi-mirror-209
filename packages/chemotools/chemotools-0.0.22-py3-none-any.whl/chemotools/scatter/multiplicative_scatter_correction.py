import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin, OneToOneFeatureMixin
from sklearn.utils.validation import check_is_fitted

from chemotools.utils.check_inputs import check_input


class MultiplicativeScatterCorrection(OneToOneFeatureMixin, BaseEstimator, TransformerMixin):
    """Multiplicative scatter correction (MSC) is a preprocessing technique for
    removing scatter effects from spectra. It is based on fitting a linear
    regression model to the spectrum using a reference spectrum. The reference
    spectrum is usually a mean or median spectrum of a set of spectra.

    Parameters
    ----------
    reference : np.ndarray, optional
        The reference spectrum to use for the correction. If None, the mean
        spectrum will be used. The default is None.
    use_mean : bool, optional
        Whether to use the mean spectrum as the reference. The default is True.
    use_median : bool, optional
        Whether to use the median spectrum as the reference. The default is False.

    Attributes
    ----------
    reference_ : np.ndarray
        The reference spectrum used for the correction.
    n_features_in_ : int
        The number of features in the training data.

    Raises
    ------
    ValueError
        If no reference is provided.
    
    """
    def __init__(
        self,
        reference: np.ndarray = None,
        use_mean: bool = True,
        use_median: bool = False,
    ):
        self.reference = reference
        self.use_mean = use_mean
        self.use_median = use_median

    def fit(self, X: np.ndarray, y=None) -> "MultiplicativeScatterCorrection":
        """
        Fit the transformer to the input data. If no reference is provided, the
        mean or median spectrum will be calculated from the input data.

        Parameters
        ----------
        X : np.ndarray of shape (n_samples, n_features)
            The input data to fit the transformer to.

        y : None
            Ignored.

        Returns
        -------
        self : MultiplicativeScatterCorrection
            The fitted transformer.
        """
        # Check that X is a 2D array and has only finite values
        X = check_input(X)

        # Set the number of features
        self.n_features_in_ = X.shape[1]

        # Set the fitted attribute to True
        self._is_fitted = True

        # Set the reference
        if self.reference is None and self.use_mean:
            self.reference_ = X.mean(axis=0)
            return self

        if self.reference is None and self.use_median:
            self.reference_ = np.median(X, axis=0)
            return self

        if self.reference is not None:
            self.reference_ = self.reference.copy()
            return self

        raise ValueError("No reference was provided")

    def transform(self, X: np.ndarray, y=None) -> np.ndarray:
        """
        Transform the input data by applying the multiplicative scatter
        correction.

        Parameters
        ----------
        X : np.ndarray of shape (n_samples, n_features)
            The input data to transform.

        y : None
            Ignored.

        Returns
        -------
        X_ : np.ndarray of shape (n_samples, n_features)
            The transformed data.
        """
        # Check that the estimator is fitted
        check_is_fitted(self, "_is_fitted")

        # Check that X is a 2D array and has only finite values
        X = check_input(X)
        X_ = X.copy()

        # Calculate the multiplicative signal correction
        ones = np.ones(X.shape[1])
        for i, x in enumerate(X_):
            X_[i] = self._calculate_multiplicative_correction(x, ones)
        return X_.reshape(-1, 1) if X_.ndim == 1 else X_

    def _calculate_multiplicative_correction(self, x, ones) -> np.ndarray:
        A = np.vstack([self.reference_, ones]).T
        m, c = np.linalg.lstsq(A, x, rcond=None)[0]
        return (x - c) / m
