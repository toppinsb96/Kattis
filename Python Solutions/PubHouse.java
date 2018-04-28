import java.util.*;

public class PubHouse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String[] parts = line.split(" ");
        Integer n = Integer.parseInt(parts[0]);
        Integer m = Integer.parseInt(parts[1]);

        //0 house, 1 pub, -1 unassigned
        int[] a = new int[n];
        for(int i = 0; i < n; i++) {
            a[i] = -1;
        }

        Map<Integer, ArrayList<Integer> > arc = new HashMap<Integer, ArrayList<Integer> >();

        for(int i = 0; i < m; i++) {
            line = sc.nextLine();
            parts = line.split(" ");
            Integer x = Integer.parseInt(parts[0]) - 1;
            Integer y = Integer.parseInt(parts[1]) - 1;

            if(arc.containsKey(x)) {
                arc.get(x).add(y);
            } else {
                System.out.println("adding array to: " + x);
                ArrayList<Integer> f = new ArrayList<Integer>();
                f.add(y);
                arc.put(x, f);
                System.out.println(arc.get(x));
            }
        }
        int[] solution = CSP(arc, a);
        printSol(solution);

    }

    static void printSol(int[] solution) {
        if(solution[0] == -1) {
            System.out.println("Impossible");
        }else {
            String s = "";
            for(int i = 0; i < solution.length;i++) {
                if(solution[i] == 0) {
                    s += "house ";
                }
                else {
                    s += "pub ";
                }
            }
            s = s.trim();
            System.out.println(s);
        }
    }

    static Boolean consistent(int[] a, Map<Integer, ArrayList<Integer> > arc) {
        for(int i = 0; i < a.length; i++) {
            if(a[i] == 0) { //house
                ArrayList<Integer> f = arc.get(new Integer(i));

                System.out.println(f);
                Boolean pubfound = false;
                for(Integer x : f) {
                    if(a[x] == 1) { // pub
                        pubfound = true;
                        break;
                    }
                }
                if(!pubfound) {
                    return false;
                }
            }
        }
        return true;
    }

    static Boolean complete(int[] c) {
        for(int i = 0; i < c.length; i++) {
            if(c[i] != 0 && c[i] != 1) { // unassigned
                return false;
            }
        }

        return true;
    }

    static int[] CSP(Map<Integer, ArrayList<Integer> > arc, int[] a) {
        for(int i = 0; i < a.length; i++) {
            for(int j = 0; j < 2; j++) { //0 house, 1 pub, -1 unassigned
                int[] b = copyArray(a);
                b[i] = j;
                if(consistent(b, arc)) {
                    int[] c = CSP(arc, b);
                    if(complete(c)) {
                        return c;
                    }
                }
            }
        }
        int[] bad = new int[1];
        bad[0] = -1;
        return bad;
    }

    static int[] copyArray(int[] a) {
        int[] b = new int[a.length];
        for(int i = 0; i < a.length; i++) {
            b[i] = a[i];
        }
        return b;
    }
}
