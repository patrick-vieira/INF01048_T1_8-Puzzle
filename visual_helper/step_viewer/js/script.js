const state = {
  current: "",
  availableMoves: "",
  spaceLocation: ""
}


actions_limits = {
  esquerda: [0, 3, 6],
  direita: [2, 5, 8],
  acima: [0, 1, 2],
  abaixo: [6, 7, 8],
}


actions_movement_offset_map = {
  esquerda: -1,
  direita: 1,
  acima: -3,
  abaixo: 3
}


let ul = document.querySelectorAll('li');;
const symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "_"]

let moves
let totalMovesSlider = document.getElementById("total_moves")

let logMoves

function setUp() {
  setId(ul)

  inputMoves = document.getElementById("moves").value.trim()
  moves = inputMoves.split(" ")
  totalMovesSlider.setAttribute("max",moves.length.toString())

  state.current = document.getElementById("initialState").value;
  state.availableMoves = get_successor_states(state.current)
  state.spaceLocation = get_current_space_location(state.current) 
  
  
  if(state.current.length > 0) {
    fillGrid(ul, state.current.split(""));
  } else {
    fillGridShuffled(ul, symbols);
  }

  draw_empty_space(state.current, state.current)
}

function validMovement(state, movement){
  if(movement in state.availableMoves) {  
    return true
  } else {
    alert("invalid move: " + movement + " - for state: " + state.current)
    return false
  }
}

function executeMovement(state, movement) {
    currentState = state.current
    nextState = state.availableMoves[movement]
    
    state.current = nextState;

    fillGrid(ul, state.current);
    
    state.availableMoves = get_successor_states(state.current)
    state.spaceLocation = get_current_space_location(state.current) 

    draw_empty_space(nextState, currentState)

    if(logMoves)
      console.log("Move: " + movement + " - from state: " + currentState + "to state: " + nextState)

    return true
  
}

function get_successor_states(current_state) {
    successor_states = new Object();

    for(action in actions_limits){
        action_limits = actions_limits[action]

        if(!is_on_border_limits(current_state, action_limits)){
            move_to = action
            successor_states[move_to] = get_next_state_from_move_direction(current_state, move_to)
        }
    }

    return successor_states
}


function is_on_border_limits(state, border_limits) {
    current_space_location = get_current_space_location(state)

    for(border_limit in border_limits){
        if (current_space_location == border_limits[border_limit])
            return true
    }

    return false
}


function get_current_space_location(current_state) {
  spaceLocation = current_state.search("_")
  return spaceLocation
}

function draw_empty_space(newState,oldState) {
  oldLocation = get_current_space_location(oldState)
  newLocation = get_current_space_location(newState)

  document.getElementById(`li${oldLocation}`).classList.remove('empty');
  document.getElementById(`li${newLocation}`).classList.add('empty');
}

function get_next_state_from_move_direction(state, move_direction) {
    current_space_location = get_current_space_location(state)
    next_space_location = current_space_location + actions_movement_offset_map[move_direction]
        
    moved_piece_symbol = state[next_space_location]

    state_list = state.split("") 

    state_list[current_space_location] = moved_piece_symbol
    state_list[next_space_location] = "_"

    new_state = state_list.join("")
 

    return new_state

}


// this function sets a unique id for each list item, in the form 'li0' to 'li8'
const setId = (items) => {
    for(let i = 0; i < items.length; i++) {
        items[i].setAttribute("id", `li${i}`)
        items[i].classList.remove('empty')
    }
}

const fillGridShuffled = (items, letters) => {
  let shuffled = shuffle(letters);

  while(!isSolvable(shuffled)) {
      shuffled = shuffle(letters);
  }

  items.forEach((item, i) => {
      item.innerText = shuffled[i];
  })
}

const fillGrid = (items, letters) => {  
  items.forEach((item, i) => {
      item.innerText = letters[i];
      if(letters[i] == i+1 || letters[-1] == "_") {
        item.style.background = "#50ad50"
      } else if (letters[i] == "_" ) {
        item.style.background = "#c5c5c5"
      } else {
        item.style.background = "#7d7b7b"
      }
  })
}

const isCorrect = (solution, content) => {
  if(JSON.stringify(solution) == JSON.stringify(content)) return true;
  return false;
}

// shuffle the array
const shuffle = (arr) => {
  const copy = [...arr];
  // loop over the array
  for(let i = 0; i < copy.length; i++) {
      // for each index,i pick a random index j 
      let j = parseInt(Math.random()*copy.length);
      // swap elements at i and j
      let temp = copy[i];
      copy[i] = copy[j];
      copy[j] = temp;
  }   
  return copy;
}

function sleep(delay) {
  var start = new Date().getTime();
  while (new Date().getTime() < start + delay);
}

function run() {  
  setUp()
  logMoves = false
  for(move in moves) {
    if(validMovement(state, moves[move]))
      executeMovement(state, moves[move])
    else 
      break    
  }
}

function runAnimated() {  
  setUp()
  logMoves = false
  window.requestAnimationFrame(step);  
}

let start;
function step(timestamp) {
  if (start === undefined)
    start = timestamp;
  const elapsed = timestamp - start;

  move = moves.shift()

  if(move && validMovement(state, move)){
    executeMovement(state, move)
    window.requestAnimationFrame(step);
  }

  totalMovesSlider.value = moves.length

  sleepTime = parseInt(document.getElementById('sleep').value)
  if(sleepTime > 1) 
    sleep(sleepTime)
}

setUp()