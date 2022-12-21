#include<cstdio>
#include<cmath>
#include<set>
#include<vector>
#include<iostream>
#include <algorithm>
#include <utility>
#include<list>
#include<iterator>

using namespace std;
const int bounds = 4000001;

list<pair < int , int > > range[bounds];

bool ok(int x , int y){
    return (x >= 0 && x < bounds && y >= 0 && y < bounds);
}

int distn(int x1, int y1, int x2, int y2){
    int dx = fabs(x1 - x2);
    int dy = fabs(y1 - y2);        
    int dist = dx + dy;
    return dist;
}

void print_list(int i){
    cout <<"Lista: " ;
    for (auto j = range[i].begin(); j!= range[i].end(); j++){
        cout <<(*j).first <<" -> " <<(*j).second <<", ";
    }
    cout <<endl;
}

void evaluate(){/*
    for(int i = 0; i < bounds; i++){
        printf("%2d" , i);
        for(int k = 0; k < bounds; k++){
            bool prazno = true;
            for (auto j = range[i].begin(); j!= range[i].end(); j++){
                if (k >= (*j).first && k <= (*j).second){
                    prazno = false;
                }
            }
            if(prazno)cout <<".";
            else cout <<"#";            
        }
        cout <<endl; 
    }*/
}


void insert_into_list(int start, int end, int row){
    
    if (start < 0){
        start = 0;
    }
    if (end >= bounds){
        end = bounds - 1;
    }
    if (start > bounds || end < 0)return;
    pair <int, int> newp = make_pair(start, end);
    bool del = false;
//    cout <<"            pri ulazu u funkciju ";
//    print_list(row);
    if(range[row].size() == 0){
        range[row].push_back(newp);
        auto ubac = range[row].begin();
//        cout <<"            ubacio sam u praznu listu " <<(*ubac).first <<" -> " <<(*ubac).second <<"\n";
        return;
    }
//    cout <<"            do tu sam dosao i sad ulazim u petlju\n";
    list< list < pair<int, int> > :: iterator > toDelete = {};
    list < pair<int, int> > :: iterator p = range[row].begin();
    bool ubacen = false;
    for (auto i = range[row].begin(); i!= range[row].end(); i++){
        pair <int, int> tmpp = *i;

//        if(row == 16 && start == 8 )cout <<start <<" " <<end <<" " <<tmpp.first <<" " <<tmpp.second <<"\n";
        
        if(!del && tmpp.first == start && tmpp.second == end)return;
        
        if (!del &&tmpp.first >= start){
            /*
            if( tmpp.second > end && tmpp.first - end <= 1){
                end = tmpp.second;
                newp.second = end;
            }*/
            auto ubac = range[row].emplace(i , newp);
            ubacen = true;
            p = ubac;
            del = true;
//            cout <<"                ubacio sam " <<(*ubac).first <<" -> " <<(*ubac).second <<"\n";
        }
        
        
        
        if (del && (tmpp.second <= end) ){
//            cout <<"                obrisao sam " <<(*i).first <<" -> " <<(*i).second <<"\n";
            toDelete.push_back(i);
            
        }   
        else if(del){
            break;
        }
        
//        cout <<"            evo zavrsio sam cak i iteraciju\n";
    }
    auto it = range[row].end(); it--;
    
    if(!del && (*it).first < start && (*it).second < end){
        range[row].push_back(newp);
        p = range[row].end();
        p--;
        ubacen = true;
//        cout <<"                ubacio sam " <<start <<" -> " <<end <<" na kraj\n";    
    } 
           
    for (auto j = toDelete.begin(); j != toDelete.end(); j++){
        range[row].erase(*j);
    }
    it = range[row].end(); it--;
//    cout <<"            prije regularizacije ";
//    print_list(row);
    if( ubacen ){
        bool delp = false;
        bool deli = false;
        if( p != range[row].begin()){
//            cout <<"      f      moj p je (" <<(*p).first <<"," <<(*p).second <<")\n";
            p--;
            auto prosli = p;
            p++;
//            cout <<"            moj p je (" <<(*p).first <<"," <<(*p).second <<"), a moj prosli je (" <<(*prosli).first <<"," <<(*prosli).second <<")\n";
            if ((*p).first - (*prosli).second <= 1){
                delp = true;
                (*p).first = (*prosli).first;
                if((*p).second < (*prosli).second){
                    (*p).second = (*prosli).second;
                }
            }
        }
        if( p != it){
//            cout <<"            moj p je (" <<(*p).first <<"," <<(*p).second <<")\n";
            p++;
            auto iduci = p;
            p--;
//            cout <<"            moj p je (" <<(*p).first <<"," <<(*p).second <<"), a moj iduci je (" <<(*iduci).first <<"," <<(*iduci).second <<")\n";
            if ((*p).second - (*iduci).first > -1){
                deli = true;
                (*p).second = (*iduci).second;
                if((*p).first > (*iduci).first){
                    (*p).first = (*iduci).first;
                }
            }
        }
        
        if(delp){
            auto izb = p; 
            izb--;
            range[row].erase( izb );
//            cout <<"            briesem proslog";
        }
        if(deli){
            p++;
            range[row].erase( p );
//            cout <<"            briesem iduceg";
        }
               
    }
    
//    cout <<"            prije izlaza iz funkcije " ;   
//    print_list(row);

    return;    
}

int main(){
    int x1;
    int y1;
    int x2;
    int y2;
    while(scanf("Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d\n" , &x1, &y1, &x2, &y2) == 4){
        int dx = fabs(x1 - x2);
        int dy = fabs(y1 - y2);        
        int dist_max = dx + dy;
//        cout <<"OBRADUJEM ULAZ S ARGUMENTIMA x1=" <<x1 <<" y1=" <<y1 <<" x2=" <<x2 <<" y2=" <<y2 <<" dist_max je " <<dist_max <<"\n";
        
        for (int i = 0; i <= dist_max; i++){
//            cout <<"    Zapocinjem novu iteraciju za ulaz\n";
            if(ok(0 , y1 + i)){
//                cout <<"        pozivam insert s argumentima " <<x1 - (dist_max - i) <<", " <<x1 +(dist_max - i) << ", " <<y1 + i <<"\n";
                insert_into_list(x1 - (dist_max - i), x1 + (dist_max - i), y1 + i);
            }
            
            if(ok(0 , y1 - i)){
//                cout <<"        pozivam insert s argumentima " <<x1 - (dist_max - i) <<", " <<x1 +(dist_max - i) << ", " <<y1 - i <<"\n";
                insert_into_list(x1 - (dist_max - i), x1 + (dist_max - i), y1 - i);
            }

        }
        
//        evaluate();
    }
/*
    cout <<"NA KRAJU SAM DOBIO:\n";
    for(int i = 0; i < bounds; i++){
        cout <<i <<" == ";
        for (auto j = range[i].begin(); j!= range[i].end(); j++){
            cout  <<(*j).first <<" -> " <<(*j).second <<", ";
        }
        cout <<endl;
    }
    cout <<"GRAFICKI PRIKAZ:\n";
    evaluate();
*/    
    long long sol;
    for (int i = 0; i < bounds; i++){
        if(range[i].size() == 2){
            auto pr = range[i].begin();
            int st = (*pr).second + 1;
            sol = (long long) 4000000 * st + i;
            cout <<i <<" " <<st <<endl;
            break;
        }
    }
    cout <<sol <<endl;
    //evaluate();
    return 0;
}
