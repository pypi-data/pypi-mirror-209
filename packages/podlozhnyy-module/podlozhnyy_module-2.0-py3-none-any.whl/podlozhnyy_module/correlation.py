from scipy.stats import t as student

from podlozhnyy_module import pd, sns, plt

def plot_corr_matrix(
    df: pd.core.frame.DataFrame,
    features: list = None,
    method: str = "pearson",
) -> None:
    """
    Строит матрицу корреляций признаков

    Parameters
    ----------
    df: Объект pandas.DataFrame
    features: Список признаков, взаимную корреляцию которых требуется посчитать, default=None
    method : Метод расчета корреляции {'pearson', 'kendall', 'spearman'}, default='pearson'
    """
    if features is None:
        features = df.columns[df.dtypes != "object"]
    corr = df[features].corr(method=method)
    plt.figure(figsize=(10, 10), facecolor='floralwhite')
    sns.heatmap(corr, vmax=1, square=True, annot=True, cmap='cubehelix')
    plt.title('Correlation between different features')
    bottom, top = plt.ylim()
    plt.ylim([bottom + 0.05, top - 0.05])
    plt.show()


def correlation_significance(
    df: pd.core.frame.DataFrame,
    features: list = None,
    method: str = "pearson",
) -> pd.core.frame.DataFrame:
    """
    Возвращает матрицу значимости корреляции признаков

    Parameters
    ----------
    df: Объект pandas.DataFrame
    features: Список названий признаков, если не указан - все числовые признаки, default=None
    method : Метод расчета корреляции {'pearson', 'kendall', 'spearman'}, default='pearson'
    """
    if features is None:
        features = df.columns[df.dtypes != "object"]
    corr = df[features].corr(method=method)
    rows = []
    for i in range(corr.shape[0] - 1):
        row = [None] * (i + 1)
        for j in range(i + 1, corr.shape[0]):
            r = corr.iloc[i, j]
            n = df[df[corr.index[i]].notnull() & df[corr.index[j]].notnull()].shape[0]
            t = (r * (n - 2) ** 0.5) / max((1 - r**2) ** 0.5, 1e-3)
            row.append(2 * (1 - student.cdf(abs(t), df=n - 2)))
        rows.append(row)
    rows.append([None] * corr.shape[0])
    data = (
        pd.DataFrame(rows, index=corr.index, columns=corr.columns)
        .fillna(0)
        .apply(round, args=(3,))
    )
    return data + data.T
