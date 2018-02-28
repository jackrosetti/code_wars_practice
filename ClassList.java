import java.util.*;
import java.io.*;
public class ClassList 
{ 
    public static void main(String[] args) throws IOException
    {
        ArrayList<String> names = new ArrayList<String>();
        Scanner scanFile = new Scanner(new File("names1.io"));
        while(scanFile.hasNext())
        {
             //System.out.println(scanFile.next());
             names.add(scanFile.next());
        }
        printEm(names);
        System.out.println(partners(names));
    }
    
    private static void printEm(ArrayList<String>names)
    {
        System.out.println(names);
    }
    
    private static String partners(ArrayList<String> names)
    {
        Random r = new Random();
        int randInt = r.nextInt(names.size());
        String first = names.get(randInt);
        names.remove(randInt);
        int randInt1 = r.nextInt(names.size());
        String partners = first + " and " + names.get(randInt1) + " are partners!";
        return partners;

    }
}