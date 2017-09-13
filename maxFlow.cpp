#include <iostream>
#include <algorithm>
#include <vector>

#define MAX_N 10000
#define MAX_V 10000
#define INF 10000

using namespace std;

struct edge {
	int to, cap, rev;
	//target of edge, remaining capbility, link to the reversed edge
};

vector<edge> G[MAX_V];
bool used[MAX_V];//visited point

void add_edge(int from, int to, int cap) {
	G[from].push_back(edge{to, cap, (int) G[to].size()});
	G[to].push_back(edge{from, 0, (int) G[from].size()-1 });
}

int dfs(int v, int t, int f) {
	if (v == t) return f;
	used[v] = true;
	for (int i = 0; i < G[v].size(); i++) {
		edge &e = G[v][i];
		if (!used[e.to] && e.cap > 0) {
			int d = dfs(e.to, t, min(f, e.cap));
			if (d > 0) {
				e.cap -= d;
				G[e.to][e.rev].cap += d;
				return d;
			}
		}
	}
	return 0;
}

int max_f(int s, int t) {
	int flow = 0;
	for (;;) {
		memset(used, 0, sizeof(used));
		int f = dfs(s, t, INF);
		if (f == 0) return flow;
		flow += f;
	}
}

int main() {
	int num_points, from, to, cap;
	cout << "Number of edges:";
	cin >> num_points;
	cout << "From To Capacity"<<endl;
	for (int i = 0; i < num_points; i++) {
		cin >> from >> to >> cap;
		add_edge(from, to, cap);
	}

	cout << max_f(0, 4)<<endl;
	
	cout << "ds";

	return 0;
}