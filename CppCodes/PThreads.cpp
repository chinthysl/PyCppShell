#include<iostream>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h>
 
using namespace std;
 
static pthread_mutex_t mutex;
 
void* printTid(void *id)
{
    pthread_mutex_lock(&mutex);
    cout <<"I'm a new thread, I'm number:" << (long)id << "(" << (unsigned int)pthread_self() << ")" << endl;
    sleep( 1 + rand() % 10);
    pthread_mutex_unlock(&mutex);
    pthread_exit(NULL);
}
 
int main()
{
    cout << "Insert number of thread to be created:";
    int numberOfThreads;
    cin >> numberOfThreads;
    
    if(numberOfThreads > 1000 || numberOfThreads < 1)
    {
        cout << "Invalid number of thread count:" << numberOfThreads << endl;
        exit(EXIT_FAILURE);
    }
    
    pthread_t* threads = new pthread_t[numberOfThreads];
 
    for(int i = 0; i < numberOfThreads; i++)
    {
        int t = pthread_create(&threads[i], NULL, printTid, (void*)i);
 
        if (t != 0)
        {
            cout << "Error in thread creation: " << t << endl;
        }
    }
 
    for(int i = 0 ; i < numberOfThreads; ++i)
    {
        void* status;
        int t = pthread_join(threads[i], &status);
        if (t != 0)
        {
            cout << "Error in thread join: " << t << endl;
            
        }
        cout << "Theard ID:" << i << " exited. Return code:" << t << endl;
    }
    
    delete[] threads;
 
    return 0;
}
