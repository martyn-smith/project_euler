;Find the sum of all the multiples of 3 or 5 below 1000. (fizzbuzz++)
(defn divisible? 
[number divisor]
    (zero? (mod number divisor))
)

(defn fizzable?
[number]
    (some true? (map (partial divisible? number) '(3 5)))
)

(defn E1 
[max_num]
    (reduce + (filter fizzable? (range max_num)))
)

(println (format "%d" (E1 1000)))