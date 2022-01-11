# Find the sum of all the multiples of 3 or 5 below 1000 (fizzbuzz++)

def euler_1(n)
  return (0..n-1).select {|i| i % 3 == 0 || i % 5 == 0 }.sum
end

puts euler_1(1000)
