#generate series(1,3,4...up to n terms)
def generate_series_odd(a: int):
    series=[]
    for i in range(a):
        series.append(2*i+1)
    return series
print(generate_series_odd(1))
print(generate_series_odd(2))
print(generate_series_odd(3))
print(generate_series_odd(4))