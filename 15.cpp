#include<cstdio>
#include<cmath>
#include<set>
#include<vector>
#include<iostream>
#include <algorithm>
#include <utility>

bool tablica[250][250];
std::vector < pair <int , int> > rangeovi[4000000];

bool ok(int x , int y){
    return (x >= 0 && x < 20 && y >= 0 && y < 20);
}

int distn(int x1, int y1, int x2, int y2){
    int dx = fabs(x1 - x2);
    int dy = fabs(y1 - y2);        
    int dist = dx + dy;
    return dist;
}

int main(){
    int x1;
    int y1;
    int x2;
    int y2;
    int thep = 2000000;
    std::set <int> points;
    std::set <int> beacons;
    
    	    
    
    while(scanf("Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d\n" , &x1, &y1, &x2, &y2) == 4){
        int dx = fabs(x1 - x2);
        int dy = fabs(y1 - y2);        
        int dist_max = dx + dy;
        if(y2 == thep){
            beacons.insert(x2);
        }
        if(y1 == thep){
            beacons.insert(x1);
        }
        
        for (int i = 0; i <= dist_max; i++){
            rangeovi[x1 + dist].push_back(make_pair(y1 - (dist_max - i), y1 + (dist_max - i)));
            update(x1 + dist , )
        }
        
        /*
        for (int dist = 0; dist <= dist_max; dist++){
            for (int ddx = 0; ddx <= dist; ddx++){
                if( ok(x1 + ddx , y1 + dist - ddx) ){
                    tablica[x1 + ddx][y1 + dist - ddx] = 1;
                }
                if( ok(x1 + ddx , y1 - dist + ddx) ){
                    tablica[x1 + ddx][y1 - dist + ddx] = 1;
                }
                if( ok(x1 - ddx , y1 + dist - ddx) ){
                    tablica[x1 - ddx][y1 + dist - ddx] = 1;
                }
                if( ok(x1 - ddx , y1 - dist + ddx) ){
                    tablica[x1 - ddx][y1 - dist + ddx] = 1;
                }
            }
          */  
            /*
            if (y1 <= thep && y1 + dist >= thep){
                int pom = dist - (thep - y1);
                points.insert(x1 + pom);
                points.insert(x1 - pom);
//                printf("dodajem (%d , %d) iz senzora (%d , %d)\n" , x1 + pom , thep , x1 , y1);
//                printf("dodajem (%d , %d) iz senzora (%d , %d)\n" , x1 - pom , thep , x1 , y1);                
            }
        
            if (y1 >= thep && y1 - dist <= thep){
                int pom = dist - (y1 - thep);
                points.insert(x1 + pom);
                points.insert(x1 - pom);
//                printf("dodajem (%d , %d) iz senzora (%d , %d)\n" , x1 + pom , thep , x1 , y1);
//                printf("dodajem (%d , %d) iz senzora (%d , %d)\n" , x1 - pom , thep , x1 , y1);                

            }
        
        }
*/
    }
    
    /*
    std::set<int>::iterator itr;
    int sol = 0;
    for (itr = points.begin(); itr != points.end(); itr++) {
        if(beacons.count(*itr)){
            continue;
        }
        sol++;
//        std::cout << *itr << " ";
    }
    
    printf("\nkolicina je %d\n" , sol);
    */
    int sol = 0;
    for(int i = 0; i < 20; i++){
        for(int j = 0; j < 20; j++){
            printf("%d " , tablica[i][j]);
            if (tablica[i][j] == 0){
                sol = 4000000 * i + j;
            }
        }
        printf("\n");
    }
    printf("SOL JE %d\n" , sol);
    return 0;
}
