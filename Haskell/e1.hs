fizzable :: Integer -> Bool
euler1 :: Integer

fizzable x = 
    let fizzers = [3, 5]

euler1 = 
    sum $ filter $ fizzable [1..999]