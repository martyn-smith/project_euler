;Find the sum of even-numbered fibonacci terms below four million.

;TODO: fix this helper function.
(defn sc_notation
[digit power]
    (* digit (reduce * (repeat 10 power)))
)

(def fibonacci
     (lazy-cat [0 1] (map + (rest fibonacci) fibonacci))
)

(defn E2 
[max_num]
    (reduce + (filter even? (take-while #(< % max_num) fibonacci)))
)

(println (format "%d" (E2 4000000)))