;Find the sum of even-numbered fibonacci terms below four million.
(defn sc_notation
[digit power]
    (* digit (reduce * (repeat 10 power)))
)

(defn fibonacci
[max_num]
    ()
)

(defn E2 
[max_num]
    (reduce + (filter even? (fibonacci max_num)))
)

(println (format "%d" (E2 (sc_notation 1 6))))