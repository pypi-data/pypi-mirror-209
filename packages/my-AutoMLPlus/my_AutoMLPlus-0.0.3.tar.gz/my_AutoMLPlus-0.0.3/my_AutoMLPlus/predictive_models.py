from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression, ElasticNet, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# абстрактный класс для всех моделей
class BaseModel(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fit(self, X_train, y_train):
        pass

    @abstractmethod
    def predict(self, X_test):
        pass


class LinearRegressionModel(BaseModel):
    def __init__(self):
        self.model = LinearRegression()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)


class ElasticNetModel(BaseModel):
    def __init__(self):
        self.model = ElasticNet()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)


class RandomForestRegressorModel(BaseModel):
    def __init__(self):
        self.model = RandomForestRegressor()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)


class GradientBoostingRegressorModel(BaseModel):
    def __init__(self):
        self.model = GradientBoostingRegressor()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)


class LogisticRegressionModel(BaseModel):
    def __init__(self):
        self.model = LogisticRegression()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)