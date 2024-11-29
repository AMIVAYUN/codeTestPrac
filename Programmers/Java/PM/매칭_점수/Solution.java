//package PM.매칭_점수;
//
//import java.util.*;
//class Solution.java {
//    /**
//
//     위상 정렬은 서로 참조하면 이뤄질 수 없다. 허나 여기엔 링크에 대한 제약조건에 단방향이라는 조건이 없다.
//
//     그럼 각 페이지별로 등록할 때 기본점수를 환산하고 페이지가 20개니깐 각각 기본점수들을 산출해서 가져오면 될 것이다.
//
//     -> 예제에도 서로 참조가 있다.
//
//     인덱스에 포함 안되는 사이트이면 링크 점수는 0점이다.
//
//     링크 점수 계산 간, 에러가 있어 TC 9 번을 뚫지 못해 참조하였습니다.
//     package PM.매칭_점수;
//
//     import java.util.*;
//     class Solution.java {
//     /**
//
//     위상 정렬은 서로 참조하면 이뤄질 수 없다. 허나 여기엔 링크에 대한 제약조건에 단방향이라는 조건이 없다.
//
//     그럼 각 페이지별로 등록할 때 기본점수를 환산하고 페이지가 20개니깐 각각 기본점수들을 산출해서 가져오면 될 것이다.
//
//     -> 예제에도 서로 참조가 있다.
//
//     인덱스에 포함 안되는 사이트이면 링크 점수는 0점이다.
//
//     링크 점수 계산 간, 에러가 있어 TC 9 번을 뚫지 못해 링크 계산 부분 참조하였습니다.
//
//
//
//     */
//    Page[] context;
//    HashMap< String, ArrayList<String> > reverse = new HashMap<>();
//    HashMap< String, Page > mapper = new HashMap<>();
//    public int solution(String word, String[] pages) {
//        int answer = 0;
//        context = new Page[ pages.length ];
//        word = word.toLowerCase();
//        int idx = 0;
//        for( String page: pages ){
//
//            int bufferIdx = 0;
//            List<String> links = new ArrayList<>();
//            int basicScore = 0;
//            int urlStart = page.indexOf("content=\"https://", page.indexOf("<meta")) + 9;
//            int urlEnd = page.indexOf("\"", urlStart);
//            String url = page.substring(urlStart, urlEnd);
//
//            while( bufferIdx < page.length() ){
//
//                if( page.charAt( bufferIdx ) == '<' ){
//                    // System.out.println("< met " );
//                    if( bufferIdx + 1 < page.length() && page.charAt( bufferIdx + 1 ) == 'a'){
//                        if(  page.substring( bufferIdx + 3, bufferIdx + 7 ).equals( "href" )){
//                            bufferIdx += 9;
//                            String temp = "";
//                            while( page.charAt( bufferIdx ) != '"'){
//                                temp += page.charAt( bufferIdx );
//                                bufferIdx++;
//                            }
//                            links.add( temp );
//                            continue;
//                        }
//                    }
//                }else if( Character.toLowerCase( page.charAt( bufferIdx ) ) == word.charAt( 0 ) ){
//                    if( bufferIdx + word.length() < page.length() ){
//                        if( page.substring( bufferIdx, bufferIdx + word.length() ).toLowerCase().equals( word ) && !isAlphabet( Character.toLowerCase( page.charAt( bufferIdx + word.length() ) ) ) && !isAlphabet( Character.toLowerCase( page.charAt( bufferIdx - 1 ) ) ) ){
//                            basicScore++;
//                            bufferIdx += word.length();
//                            continue;
//                        }
//                    }
//
//
//                }
//
//                bufferIdx++;
//            }
//            // System.out.println("index = " + idx + " url = " + url + " links = " + links.size() + ", basicScore = " + basicScore );
//            Page newPage = new Page( url, links, idx, basicScore );
//            context[ idx ] = newPage;
//            mapper.put( url, newPage );
//            idx ++;
//        }
//
//        for( Page page: context ){
//            reverse.put( page.url, new ArrayList<String>() );
//        }
//
//        for( Page page: context ){
//            for( String link: page.links ){
//                if( !reverse.containsKey( link ) ) continue;
//                ArrayList<String> from = reverse.get( link );
//                from.add( page.url );
//            }
//        }
//
//        for( Page page: context ){
//            page.calculateLinkScore();
//        }
//
//        Arrays.sort( context, ( p1, p2 ) -> {
//            if( p1.matchScore == p2.matchScore ){
//                return Integer.compare( p1.index, p2.index );
//            }
//            return Double.compare( p2.matchScore, p1.matchScore );
//        });
//
//        return context[ 0 ].index;
//    }
//
//    public boolean isAlphabet( char a ){
//        return a >= 'a' && a <= 'z';
//    }
//
//    public class Page{
//        String url;
//        List< String > links;
//        int index;
//        int basicScore;
//        double linkScore = 0.0;
//        double matchScore = 0.0;
//
//        public Page( String url, List< String > links, int index, int basicScore ){
//            this.url = url;
//            this.links = links;
//            this.index = index;
//            this.basicScore = basicScore;
//        }
//
//        @Override
//        public int hashCode() {
//            return url != null ? url.hashCode() : 0;
//        }
//
//        @Override
//        public boolean equals(Object obj) {
//            if (this == obj)
//                return true;
//            if (obj == null || getClass() != obj.getClass())
//                return false;
//            Page other = (Page) obj;
//            return url != null ? url.equals(other.url) : other.url == null;
//        }
//
//        @Override
//        public String toString(){
//            return "index = " + index + " url = " + url + " links = " + links.size() + ", basicScore = " + basicScore + " linkScore = " + linkScore;
//        }
//
//        public void calculateLinkScore(){
//            ArrayList<String> from = reverse.get( url );
//            double value = 0d;
//            for( String furl : from ){
//                Page page = mapper.get( furl );
//
//                value += ( double ) page.basicScore / (double)page.links.size();
//
//            }
//
//            this.linkScore = value;
//
//            this.matchScore = value + basicScore;
//        }
//    }
//}
//
//    Page[] context;
//    HashMap< String, ArrayList<String> > reverse = new HashMap<>();
//    HashMap< String, Page > mapper = new HashMap<>();
//    public int solution(String word, String[] pages) {
//        int answer = 0;
//        context = new Page[ pages.length ];
//        word = word.toLowerCase();
//        int idx = 0;
//        for( String page: pages ){
//
//            int bufferIdx = 0;
//            List<String> links = new ArrayList<>();
//            int basicScore = 0;
//            int urlStart = page.indexOf("content=\"https://", page.indexOf("<meta")) + 9;
//            int urlEnd = page.indexOf("\"", urlStart);
//            String url = page.substring(urlStart, urlEnd);
//
//            while( bufferIdx < page.length() ){
//
//                if( page.charAt( bufferIdx ) == '<' ){
//                    // System.out.println("< met " );
//                    if( bufferIdx + 1 < page.length() && page.charAt( bufferIdx + 1 ) == 'a'){
//                        if(  page.substring( bufferIdx + 3, bufferIdx + 7 ).equals( "href" )){
//                            bufferIdx += 9;
//                            String temp = "";
//                            while( page.charAt( bufferIdx ) != '"'){
//                                temp += page.charAt( bufferIdx );
//                                bufferIdx++;
//                            }
//                            links.add( temp );
//                            continue;
//                        }
//                    }
//                }else if( Character.toLowerCase( page.charAt( bufferIdx ) ) == word.charAt( 0 ) ){
//                    if( bufferIdx + word.length() < page.length() ){
//                        if( page.substring( bufferIdx, bufferIdx + word.length() ).toLowerCase().equals( word ) && !isAlphabet( Character.toLowerCase( page.charAt( bufferIdx + word.length() ) ) ) && !isAlphabet( Character.toLowerCase( page.charAt( bufferIdx - 1 ) ) ) ){
//                            basicScore++;
//                            bufferIdx += word.length();
//                            continue;
//                        }
//                    }
//
//
//                }
//
//                bufferIdx++;
//            }
//            // System.out.println("index = " + idx + " url = " + url + " links = " + links.size() + ", basicScore = " + basicScore );
//            Page newPage = new Page( url, links, idx, basicScore );
//            context[ idx ] = newPage;
//            mapper.put( url, newPage );
//            idx ++;
//        }
//
//        for( Page page: context ){
//            reverse.put( page.url, new ArrayList<String>() );
//        }
//
//        for( Page page: context ){
//            for( String link: page.links ){
//                if( !reverse.containsKey( link ) ) continue;
//                ArrayList<String> from = reverse.get( link );
//                from.add( page.url );
//            }
//        }
//
//        for( Page page: context ){
//            page.calculateLinkScore();
//        }
//
//        Arrays.sort( context, ( p1, p2 ) -> {
//            if( p1.matchScore == p2.matchScore ){
//                return Integer.compare( p1.index, p2.index );
//            }
//            return Double.compare( p2.matchScore, p1.matchScore );
//        });
//
//        return context[ 0 ].index;
//    }
//
//    public boolean isAlphabet( char a ){
//        return a >= 'a' && a <= 'z';
//    }
//
//    public class Page{
//        String url;
//        List< String > links;
//        int index;
//        int basicScore;
//        double linkScore = 0.0;
//        double matchScore = 0.0;
//
//        public Page( String url, List< String > links, int index, int basicScore ){
//            this.url = url;
//            this.links = links;
//            this.index = index;
//            this.basicScore = basicScore;
//        }
//
//        @Override
//        public int hashCode() {
//            return url != null ? url.hashCode() : 0;
//        }
//
//        @Override
//        public boolean equals(Object obj) {
//            if (this == obj)
//                return true;
//            if (obj == null || getClass() != obj.getClass())
//                return false;
//            Page other = (Page) obj;
//            return url != null ? url.equals(other.url) : other.url == null;
//        }
//
//        @Override
//        public String toString(){
//            return "index = " + index + " url = " + url + " links = " + links.size() + ", basicScore = " + basicScore + " linkScore = " + linkScore;
//        }
//
//        public void calculateLinkScore(){
//            ArrayList<String> from = reverse.get( url );
//            double value = 0d;
//            for( String furl : from ){
//                Page page = mapper.get( furl );
//
//                value += ( double ) page.basicScore / (double)page.links.size();
//
//            }
//
//            this.linkScore = value;
//
//            this.matchScore = value + basicScore;
//        }
//    }
//}