class Node {
	constructor(data) {
		this.data = data;
		this.next = null;
	}
}

class Queue {
	constructor() {
		this.head = this.tail = null;
		this.size = 0;
	}

	enqueue(data) {
		const node = new Node(data);
		if (this.is_empty()) {
			this.head = this.tail = node;
		} else {
			this.tail = this.tail.next = node;
		}
		this.size++;
	}

	is_empty() {
		return this.size == 0;
	}

	toArray() {
		const nodeArray = [];
		let curNode = this.head;
		while (curNode != null) {
			nodeArray.push(curNode.data);
			curNode = curNode.next;
		}
		return nodeArray;
	}
}

const socket = io.connect('http://' + document.domain + ':' + location.port);
const history = new Queue();

document.addEventListener('DOMContentLoaded', () => {
    const notePlayed = document.getElementById('noteBeingPlayed');
    const noteFeed = document.getElementById('noteFeed');

    socket.emit('connected');

    socket.on('onNotePlayed', (msg) => {
        const { note, velocity, location } = msg;
        console.log({ note, velocity, location });
        
        notePlayed.textContent = note;
        updateHistory(note);
    });

	function updateHistory(note) {
		history.enqueue(note);
	
		const span = document.createElement('span');
		span.textContent = note;
		noteFeed.appendChild(span);
	
		setTimeout(() => {
			if (noteFeed.firstChild) {
				noteFeed.removeChild(noteFeed.firstChild);
			}
		}, 10000);
	}
});
