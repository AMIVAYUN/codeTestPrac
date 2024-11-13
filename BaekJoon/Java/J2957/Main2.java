package J2957;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main2 {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[] memo = new int[ 300_001 ];
    static ArrayList<Integer> nums = new ArrayList<>();
    static long cnt;
    public static void main(String[] args) throws IOException {
        RedBlackTree rbTree = new RedBlackTree();

        int n = Integer.parseInt( bf.readLine() );
        StringBuilder sb = new StringBuilder();
        for( int i = 0; i < n; i ++ ){
            int k = Integer.parseInt( bf.readLine() );
            rbTree.insert( k );
            insort( nums, k );

            sb.append( cnt );
            if( i != n - 1 ){
                sb.append("\n");
            }

        }

        System.out.print(sb);
    }

    public static void insort(ArrayList<Integer> list, int value) {
        if( list.size() == 0 ){
            list.add( value );
            return;
        }

        if( list.get( 0 ) > value ){
            cnt += memo[list.get(0)] + 1;
            memo[ value ] = memo[list.get(0)] + 1;
            list.add( 0, value );
            return;
        }else if( list.get( list.size() - 1 ) < value ){
            cnt += memo[ list.get( list.size() - 1 ) ] + 1;
            memo[ value ] = memo[ list.get( list.size() - 1 ) ] + 1;
            list.add( value );
            return;
        }


        int lt = 0; int rt = list.size() - 1;

        while( lt <= rt ){
            int mid = ( lt + rt ) / 2;

            if (list.get(mid) < value) {
                lt = mid + 1;
            } else {
                rt = mid - 1;
            }
        }

        list.add( lt, value );

        int ltValue = lt != 0 ? memo[ list.get(lt - 1) ] : 0;
        int rtValue = lt + 1 != list.size() ? memo[ list.get(lt + 1) ] : 0;

        cnt += Math.max( ltValue, rtValue ) + 1;
        memo[ value ] = Math.max( ltValue, rtValue ) + 1;
    }

    static class RedBlackTree {

        private final int RED = 0;
        private final int BLACK = 1;

        class Node {
            int data, color;
            Node left, right, parent;

            Node(int data) {
                this.data = data;
                this.color = RED;
                this.left = null;
                this.right = null;
                this.parent = null;
            }
        }

        private Node root;

        public RedBlackTree() {
            root = null;
        }


        private void leftRotate(Node node) {
            Node rightChild = node.right;
            node.right = rightChild.left;

            if (rightChild.left != null) {
                rightChild.left.parent = node;
            }

            rightChild.parent = node.parent;

            if (node.parent == null) {
                root = rightChild;
            } else if (node == node.parent.left) {
                node.parent.left = rightChild;
            } else {
                node.parent.right = rightChild;
            }

            rightChild.left = node;
            node.parent = rightChild;
        }

        private void rightRotate(Node node) {
            Node leftChild = node.left;
            node.left = leftChild.right;

            if (leftChild.right != null) {
                leftChild.right.parent = node;
            }

            leftChild.parent = node.parent;

            if (node.parent == null) {
                root = leftChild;
            } else if (node == node.parent.right) {
                node.parent.right = leftChild;
            } else {
                node.parent.left = leftChild;
            }

            leftChild.right = node;
            node.parent = leftChild;
        }


        public void insert(int data) {
            Node node = new Node(data);
            root = bstInsert(root, node);
            fixInsert(node);
        }


        private Node bstInsert(Node root, Node node) {
            if (root == null) {
                return node;
            }

            if (node.data < root.data) {
                root.left = bstInsert(root.left, node);
                root.left.parent = root;
            } else if (node.data > root.data) {
                root.right = bstInsert(root.right, node);
                root.right.parent = root;
            }

            return root;
        }


        private void fixInsert(Node node) {
            Node parent = null;
            Node grandParent = null;

            while (node != root && node.color == RED && node.parent.color == RED) {
                parent = node.parent;
                grandParent = parent.parent;

                if (parent == grandParent.left) {
                    Node uncle = grandParent.right;

                    if (uncle != null && uncle.color == RED) {
                        grandParent.color = RED;
                        parent.color = BLACK;
                        uncle.color = BLACK;
                        node = grandParent;
                    } else {
                        if (node == parent.right) {
                            leftRotate(parent);
                            node = parent;
                            parent = node.parent;
                        }

                        rightRotate(grandParent);
                        int temp = parent.color;
                        parent.color = grandParent.color;
                        grandParent.color = temp;
                        node = parent;
                    }
                } else {
                    Node uncle = grandParent.left;

                    if (uncle != null && uncle.color == RED) {
                        grandParent.color = RED;
                        parent.color = BLACK;
                        uncle.color = BLACK;
                        node = grandParent;
                    } else {
                        if (node == parent.left) {
                            rightRotate(parent);
                            node = parent;
                            parent = node.parent;
                        }

                        leftRotate(grandParent);
                        int temp = parent.color;
                        parent.color = grandParent.color;
                        grandParent.color = temp;
                        node = parent;
                    }
                }
            }

            root.color = BLACK;
        }


        public Node getRoot() {
            return root;
        }


    }

}