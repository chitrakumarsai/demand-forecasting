from src.logger import ProjectLogger
from statsmodels.tsa.seasonal import seasonal_decompose

class SeasonalDecomposer:
    def __init__(self, frequency):
        self.frequency = frequency
        self.logger = ProjectLogger().get_logger()

        def decompose(self, df, model="additive"):
            """
            Decompose the time series into trend, seasonal and residual components.

            Args:
                df (pd.DataFrame): DataFrame containing the time series data.
                model (str, optional): Model to use for decomposition. Defaults to "additive".

            Returns:
                DecomposeResult: Decomposed time series.
            """
            self.logger.info("Decomposing time series")
            try:
                series = df[["demand_in_MW"]]
                decomposed = seasonal_decompose(series, model=model, period=self.frequency)
                return decomposed
            except Exception as e:
                self.logger.exception(f"Error while doing seasonal decomposition: {e}")