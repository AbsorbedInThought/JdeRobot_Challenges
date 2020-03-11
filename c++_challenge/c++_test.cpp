
#include <iostream>
#include <string.h>
#include <fstream>
#include <algorithm>

using namespace std;

#define zero 48

/* Prints Array*/
void print_array(const char arr[], const int &no_of_rows, const int &no_of_cols)
{
  cout << endl;
  for(int row=0; row<no_of_rows; row++)
  {
    for(int col=0; col<no_of_cols; col++)
      cout << arr[(row*no_of_cols)+col];
    cout << endl;
  }
}

/* Calculates Paths */
unsigned short int back_track(char arr[], const unsigned short int no_of_cols, const int &current_row,
const unsigned short int &current_col, unsigned short int current_value)
{
  char current = arr[(current_row*no_of_cols)+current_col];
  unsigned short int maximum=0;
  if(current=='#')
    return current_value;

  else if(current=='.')
  {
    arr[(current_row*no_of_cols)+current_col] = current_value;
    current_value++;

    maximum=max(back_track(arr, no_of_cols, current_row,current_col-1, current_value),
    back_track(arr, no_of_cols, current_row, current_col+1, current_value));

    maximum=max(maximum, back_track(arr, no_of_cols, current_row+1, current_col, current_value));
  }
  return maximum;
}

/* Removes The Shorter Paths */
void extract_longest_path(char arr[], unsigned short int no_of_cols,
unsigned short int current_row, unsigned short int current_col)
{
  char current = arr[(current_row*no_of_cols)+current_col];
  if(current == '#')
    return;

  else if(current != '.')
  {
    arr[(current_row*no_of_cols)+current_col] = '.';
    extract_longest_path(arr, no_of_cols, current_row, current_col-1);
    extract_longest_path(arr, no_of_cols, current_row, current_col+1);
    extract_longest_path(arr, no_of_cols, current_row+1, current_col);
  }
}


int main(int argc, char *argv[])
{
  /* Reading maze from text file */
  string line;
  string rows[20]; //Upto 20 Rows
	ifstream load_maze;
	load_maze.open(argv[1]);

  unsigned short int no_of_rows = 0;

  //If file stream is good
  if(load_maze.good())
  {
    while(!load_maze.eof())
    {
       getline(load_maze,line);
       rows[no_of_rows] = line;
       no_of_rows++;
    }
    load_maze.close();
  }
  else
    cout << "Error Opening File...\n";

  /* Saving input into a character array */
  const unsigned short int no_of_cols = rows[0].length();
  char arr[no_of_rows*no_of_cols];

  cout << endl << "Input: " << endl;
  for(int row=0; row<no_of_rows; row++)
    for(int col=0; col<no_of_cols; col++)
      arr[(row*no_of_cols)+col] = rows[row][col];

  print_array(arr, no_of_rows, no_of_cols);

  short int max_path=-999;
  unsigned short int not_index=0;
  unsigned short int to_store=0;

  for(int col=0; col<no_of_cols; col++)
  {
    to_store=back_track(arr, no_of_cols, 0, col, zero)-zero;
    if(to_store > max_path)
    {
      max_path=to_store;
      not_index = col;
    }
  }

  cout << "Output: \n" << max_path << endl;

  for(int col=0; col<no_of_cols; ++col)
    if(col != not_index)
      extract_longest_path(arr, no_of_cols, 0, col);

  print_array(arr, no_of_rows, no_of_cols);

  return 0;
}
