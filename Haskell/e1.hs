fizzable :: Integer -> Bool
euler1 :: Integer

fizzable x = 
    any (\f -> x `mod` f == 0) [3, 5]

euler1 = 
    sum $ filter $ fizzable [1..999]

putStrLn $ euler1