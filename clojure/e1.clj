;;"Find the sum of all the multiples of 3 or 5 below 1000. (fizzbuzz++)"

(defn Euler1
    (def total 0)
    for [x [1 1000]
        : (+ total x)
        : when (or (not(mod x 3) not(mod x 5)))
    ]
)