import Data.List

parsiranjeUlaza :: [String] -> [Int]
parsiranjeUlaza xs = map mapFunc xs
        where mapFunc x | x !! 0 == 'a' = intg x
                        | otherwise = 0  
              intg x = read $ drop 5 x ::Int

snage :: Int -> [Int] -> [Int]
snage x [] = [x]
snage x (h:xs) | h == 0 = x:(snage x xs)
               | otherwise = x:x:(snage addX xs )
        where addX = x + h

zbr :: [Int] -> Int
zbr xs = foldl (+) 0 $ map calc [20, 60, 100, 140, 180, 220]
        where calc x | x > sz = x * ( xs !! ( sz - 1) ) 
                     | otherwise  = x * ( xs !! (x - 1))
              sz = length xs

ispis :: [Int]  -> [Char]
ispis xs = map charAt listInd
        where charAt x | snd x == fst x || snd x == fst x + 1 || snd x == fst x + 2 = '#'
                       | otherwise = '.'                       
              listInd = zip xs auxList
              auxList = cycle [1..40]



main = do
    s <- readFile "sample"
    let snageLista = snage 1 $ parsiranjeUlaza $ lines s
    let rezultat = zbr $ snage 1 $ parsiranjeUlaza $ lines s
    putStrLn $ show snageLista
    let rezultat2 = ispis snageLista
    
    putStrLn $ show $ take 40 rezultat2
    let rezultat3 = drop 40 rezultat2
    
    putStrLn $ show $ take 40 rezultat3
    let rezultat4 = drop 40 rezultat3
   
    putStrLn $ show $ take 40 rezultat4
    let rezultat5 = drop 40 rezultat4
    
    putStrLn $ show $ take 40 rezultat5
    let rezultat6 = drop 40 rezultat5
    
    putStrLn $ show $ take 40 rezultat6
    let rezultat7 = drop 40 rezultat6
    
    putStrLn $ show $ take 40 rezultat7
--    let rezultat3 = drop 40 rezultat2
    
    
