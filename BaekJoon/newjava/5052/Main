package J5052;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n;

    public static void main(String[] args) throws IOException {
        n = stoi( bf.readLine() );
        for( int i = 0; i < n; i ++ ){
            int k = stoi( bf.readLine() );
            Node trie = new Node();
            boolean isConsistent = true;

            List<String> keyList = new ArrayList<>();
            for (int j = 0; j < k; j++) {
                String str = bf.readLine();
                trie.insert(str);
                keyList.add(str);
            }

            for(String key : keyList) {
                if(trie.contains(key)) {
                    isConsistent = false;
                    break;
                }
            }
            System.out.println(isConsistent?"YES":"NO");
        }



    }

    public static int stoi(String t){
        return Integer.parseInt( t );
    }


    static class Node{
        Map< Character, Node > childNode = new HashMap<>();
        boolean terminal;

        public void insert( String word ){
            Node node = this;
            for( int i = 0; i < word.length(); i ++ ){
                char c = word.charAt( i );
                node.childNode.putIfAbsent( c, new Node() );
                node = node.childNode.get( c );

                if( i == word.length() - 1 ){
                    node.terminal = true;
                }
            }
        }


        public boolean contains(String word) {
            Node trieNode = this;
            for(int i=0; i<word.length(); i++) {
                char c= word.charAt(i);
                Node node = trieNode.childNode.get(c);

                if(node == null) {
                    return false;
                }
                trieNode = node;
            }

            // 해당 단어로 종료하는 문자가 있는 경우 false
            if(trieNode.terminal) {
                // 자기 자신 제외 (childNode가 없으면 해당 종료노드는 자기 자신임 ex) 911> 911)
                if(trieNode.childNode.isEmpty()) {
                    return false;
                }
            }
            return true;
        }
    }
}