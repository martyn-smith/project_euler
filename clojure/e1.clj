;Find the sum of all the multiples of 3 or 5 below 1000. (fizzbuzz++)
(defn divisible? 
[number divisor]
    (zero? (mod number divisor))
)

(def fizzers (3 5))

(defn E1 
[max_num]
    (reduce + (filter divisible? (range max_num) (fizzers)))
)

(println (format "%d" (E1 1000)))