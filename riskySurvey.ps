import streamlit as st
import streamlit.components.v1 as components
with open('risk-survey4.py', 'r') as f:
    html_data = f.read()
    components.html(html_data, height=1000, scrolling=True)

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Risk Preference Survey</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .user-info-form {
            background-color: #e8f4fd;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }
        .form-group {
            margin: 15px 0;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .form-group input {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
        }
        .prospect-display {
            background-color: #e8f4fd;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
        }
        .expected-value {
            color: #666;
            font-size: 16px;
            margin-top: 10px;
        }
        .choice-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px;
            margin: 10px 0;
            background-color: #f9f9f9;
            border-radius: 5px;
            border: 2px solid transparent;
        }
        .choice-item.selected {
            background-color: #e8f4fd;
            border-color: #007acc;
        }
        .choice-item.error {
            background-color: #ffe6e6;
            border-color: #ff6b6b;
        }
        .choice-text {
            font-size: 16px;
        }
        .choice-buttons {
            display: flex;
            gap: 15px;
        }
        button {
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s;
        }
        .prefer-prospect {
            background-color: #007acc;
            color: white;
        }
        .prefer-prospect:hover {
            background-color: #005999;
        }
        .prefer-prospect.selected {
            background-color: #004080;
            transform: scale(0.95);
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);
        }
        .prefer-sure {
            background-color: #28a745;
            color: white;
        }
        .prefer-sure:hover {
            background-color: #1e7e34;
        }
        .prefer-sure.selected {
            background-color: #155724;
            transform: scale(0.95);
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);
        }
        .next-button {
            background-color: #6c757d;
            color: white;
            padding: 12px 24px;
            font-size: 16px;
            margin: 20px 0;
        }
        .next-button:hover {
            background-color: #545b62;
        }
        .next-button:disabled {
            background-color: #ccc;
            cursor: not-allowed;
        }
        .start-button {
            background-color: #007acc;
            color: white;
            padding: 12px 24px;
            font-size: 16px;
            margin: 20px 0;
        }
        .start-button:hover {
            background-color: #005999;
        }
        .export-button {
            background-color: #17a2b8;
            color: white;
            padding: 12px 24px;
            font-size: 16px;
            margin: 10px 5px;
        }
        .export-button:hover {
            background-color: #138496;
        }
        .progress {
            background-color: #e9ecef;
            height: 10px;
            border-radius: 5px;
            margin: 20px 0;
        }
        .progress-bar {
            background-color: #007acc;
            height: 100%;
            border-radius: 5px;
            transition: width 0.3s;
        }
        .error-message {
            color: #dc3545;
            font-weight: bold;
            text-align: center;
            margin: 10px 0;
        }
        .instructions {
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }
        .results {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }
        .phase-indicator {
            text-align: center;
            margin: 15px 0;
            font-weight: bold;
            color: #007acc;
        }
        .domain-indicator {
            text-align: center;
            margin: 10px 0;
            font-size: 14px;
            color: #666;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Risk Preference Survey</h1>
        
        <div id="userInfoSection">
            <div class="instructions">
                <h3>Welcome to the Risk Preference Survey</h3>
                <p>This survey examines how people make decisions involving risk and uncertainty. You will be presented with a series of decision problems involving risky prospects with known probabilities.</p>
                <p>Please provide some basic information about yourself before we begin:</p>
            </div>
            
            <div class="user-info-form">
                <div class="form-group">
                    <label for="userName">Name:</label>
                    <input type="text" id="userName" required>
                </div>
                <div class="form-group">
                    <label for="userAge">Age:</label>
                    <input type="number" id="userAge" min="18" max="120" required>
                </div>
                <button class="start-button" onclick="survey.startSurvey()">Start Survey</button>
            </div>
        </div>
        
        <div id="surveySection" style="display: none;">
            <div class="instructions">
                <h3>Instructions:</h3>
                <p>You will be presented with a series of decision problems involving risky prospects with known probabilities. For each problem, you will choose between a risky prospect and various sure amounts of money.</p>
                <p>Please make your choices carefully. The computer will monitor consistency and alert you to any logical errors.</p>
            </div>

            <div class="progress">
                <div class="progress-bar" id="progressBar"></div>
            </div>
            
            <div id="problemDisplay"></div>
        </div>
        
        <div class="results" id="results" style="display: none;"></div>
    </div>

    <script>
        class ProspectSurvey {
            constructor() {
                // Table 3 prospects from 1992 paper - gains and losses
                this.allProspects = {
                    gains: [
                        { type: 'risky', outcomes: [0, 50], probabilities: [0.99, 0.01], description: '1% chance to win $50, 99% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 50], probabilities: [0.95, 0.05], description: '5% chance to win $50, 95% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 50], probabilities: [0.90, 0.10], description: '10% chance to win $50, 90% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 50], probabilities: [0.75, 0.25], description: '25% chance to win $50, 75% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 50], probabilities: [0.50, 0.50], description: '50% chance to win $50, 50% chance to win nothing' },
                        
                        { type: 'risky', outcomes: [0, 100], probabilities: [0.95, 0.05], description: '5% chance to win $100, 95% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 100], probabilities: [0.90, 0.10], description: '10% chance to win $100, 90% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 100], probabilities: [0.75, 0.25], description: '25% chance to win $100, 75% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 100], probabilities: [0.50, 0.50], description: '50% chance to win $100, 50% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 100], probabilities: [0.25, 0.75], description: '75% chance to win $100, 25% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 100], probabilities: [0.10, 0.90], description: '90% chance to win $100, 10% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 100], probabilities: [0.05, 0.95], description: '95% chance to win $100, 5% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 100], probabilities: [0.01, 0.99], description: '99% chance to win $100, 1% chance to win nothing' },
                        
                        { type: 'risky', outcomes: [0, 200], probabilities: [0.99, 0.01], description: '1% chance to win $200, 99% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 200], probabilities: [0.95, 0.05], description: '5% chance to win $200, 95% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 200], probabilities: [0.90, 0.10], description: '10% chance to win $200, 90% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 200], probabilities: [0.50, 0.50], description: '50% chance to win $200, 50% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 200], probabilities: [0.25, 0.75], description: '75% chance to win $200, 25% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 200], probabilities: [0.10, 0.90], description: '90% chance to win $200, 10% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 200], probabilities: [0.05, 0.95], description: '95% chance to win $200, 5% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 200], probabilities: [0.01, 0.99], description: '99% chance to win $200, 1% chance to win nothing' },
                        
                        { type: 'risky', outcomes: [0, 400], probabilities: [0.99, 0.01], description: '1% chance to win $400, 99% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 400], probabilities: [0.95, 0.05], description: '5% chance to win $400, 95% chance to win nothing' },
                        { type: 'risky', outcomes: [0, 400], probabilities: [0.01, 0.99], description: '99% chance to win $400, 1% chance to win nothing' },
                        
                        { type: 'risky', outcomes: [50, 100], probabilities: [0.90, 0.10], description: '10% chance to win $100, 90% chance to win $50' },
                        { type: 'risky', outcomes: [50, 100], probabilities: [0.50, 0.50], description: '50% chance to win $100, 50% chance to win $50' },
                        { type: 'risky', outcomes: [50, 100], probabilities: [0.25, 0.75], description: '75% chance to win $100, 25% chance to win $50' },
                        
                        { type: 'risky', outcomes: [50, 150], probabilities: [0.95, 0.05], description: '5% chance to win $150, 95% chance to win $50' },
                        { type: 'risky', outcomes: [50, 150], probabilities: [0.90, 0.10], description: '10% chance to win $150, 90% chance to win $50' },
                        { type: 'risky', outcomes: [50, 150], probabilities: [0.50, 0.50], description: '50% chance to win $150, 50% chance to win $50' },
                        { type: 'risky', outcomes: [50, 150], probabilities: [0.25, 0.75], description: '75% chance to win $150, 25% chance to win $50' },
                        { type: 'risky', outcomes: [50, 150], probabilities: [0.10, 0.90], description: '90% chance to win $150, 10% chance to win $50' },
                        { type: 'risky', outcomes: [50, 150], probabilities: [0.05, 0.95], description: '95% chance to win $150, 5% chance to win $50' },
                        
                        { type: 'risky', outcomes: [100, 200], probabilities: [0.95, 0.05], description: '5% chance to win $200, 95% chance to win $100' },
                        { type: 'risky', outcomes: [100, 200], probabilities: [0.90, 0.10], description: '10% chance to win $200, 90% chance to win $100' },
                        { type: 'risky', outcomes: [100, 200], probabilities: [0.50, 0.50], description: '50% chance to win $200, 50% chance to win $100' },
                        { type: 'risky', outcomes: [100, 200], probabilities: [0.25, 0.75], description: '75% chance to win $200, 25% chance to win $100' },
                        { type: 'risky', outcomes: [100, 200], probabilities: [0.10, 0.90], description: '90% chance to win $200, 10% chance to win $100' }
                    ],
                    losses: [
                        { type: 'risky', outcomes: [0, -50], probabilities: [0.90, 0.10], description: '10% chance to lose $50, 90% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -50], probabilities: [0.50, 0.50], description: '50% chance to lose $50, 50% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -50], probabilities: [0.10, 0.90], description: '90% chance to lose $50, 10% chance to lose nothing' },
                        
                        { type: 'risky', outcomes: [0, -100], probabilities: [0.95, 0.05], description: '5% chance to lose $100, 95% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -100], probabilities: [0.75, 0.25], description: '25% chance to lose $100, 75% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -100], probabilities: [0.50, 0.50], description: '50% chance to lose $100, 50% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -100], probabilities: [0.25, 0.75], description: '75% chance to lose $100, 25% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -100], probabilities: [0.05, 0.95], description: '95% chance to lose $100, 5% chance to lose nothing' },
                        
                        { type: 'risky', outcomes: [0, -200], probabilities: [0.99, 0.01], description: '1% chance to lose $200, 99% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -200], probabilities: [0.95, 0.05], description: '5% chance to lose $200, 95% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -200], probabilities: [0.50, 0.50], description: '50% chance to lose $200, 50% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -200], probabilities: [0.10, 0.90], description: '90% chance to lose $200, 10% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -200], probabilities: [0.05, 0.95], description: '95% chance to lose $200, 5% chance to lose nothing' },
                        
                        { type: 'risky', outcomes: [0, -400], probabilities: [0.99, 0.01], description: '1% chance to lose $400, 99% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -400], probabilities: [0.95, 0.05], description: '5% chance to lose $400, 95% chance to lose nothing' },
                        { type: 'risky', outcomes: [0, -400], probabilities: [0.01, 0.99], description: '99% chance to lose $400, 1% chance to lose nothing' },
                        
                        { type: 'risky', outcomes: [-50, -100], probabilities: [0.50, 0.50], description: '50% chance to lose $100, 50% chance to lose $50' },
                        { type: 'risky', outcomes: [-50, -100], probabilities: [0.25, 0.75], description: '75% chance to lose $100, 25% chance to lose $50' },
                        { type: 'risky', outcomes: [-50, -100], probabilities: [0.10, 0.90], description: '90% chance to lose $100, 10% chance to lose $50' },
                        
                        { type: 'risky', outcomes: [-50, -150], probabilities: [0.95, 0.05], description: '5% chance to lose $150, 95% chance to lose $50' },
                        { type: 'risky', outcomes: [-50, -150], probabilities: [0.90, 0.10], description: '10% chance to lose $150, 90% chance to lose $50' },
                        { type: 'risky', outcomes: [-50, -150], probabilities: [0.50, 0.50], description: '50% chance to lose $150, 50% chance to lose $50' },
                        { type: 'risky', outcomes: [-50, -150], probabilities: [0.25, 0.75], description: '75% chance to lose $150, 25% chance to lose $50' },
                        { type: 'risky', outcomes: [-50, -150], probabilities: [0.10, 0.90], description: '90% chance to lose $150, 10% chance to lose $50' },
                        { type: 'risky', outcomes: [-50, -150], probabilities: [0.05, 0.95], description: '95% chance to lose $150, 5% chance to lose $50' },
                        
                        { type: 'risky', outcomes: [-100, -200], probabilities: [0.95, 0.05], description: '5% chance to lose $200, 95% chance to lose $100' },
                        { type: 'risky', outcomes: [-100, -200], probabilities: [0.90, 0.10], description: '10% chance to lose $200, 90% chance to lose $100' },
                        { type: 'risky', outcomes: [-100, -200], probabilities: [0.50, 0.50], description: '50% chance to lose $200, 50% chance to lose $100' },
                        { type: 'risky', outcomes: [-100, -200], probabilities: [0.25, 0.75], description: '75% chance to lose $200, 25% chance to lose $100' },
                        { type: 'risky', outcomes: [-100, -200], probabilities: [0.10, 0.90], description: '90% chance to lose $200, 10% chance to lose $100' }
                    ]
                };
                
                this.userName = '';
                this.userAge = '';
                this.prospects = [];
                this.currentProspectIndex = 0;
                this.currentPhase = 1; // 1 = initial choices, 2 = refined choices
                this.choices = [];
                this.currentChoices = [];
                this.sureAmounts = [];
                this.results = [];
                this.errorMessage = '';
            }
            
            startSurvey() {
                const name = document.getElementById('userName').value.trim();
                const age = document.getElementById('userAge').value;
                
                if (!name || !age) {
                    alert('Please fill in both name and age fields.');
                    return;
                }
                
                this.userName = name;
                this.userAge = parseInt(age);
                
                // Randomly select 5 prospects from each domain
                const shuffledGains = [...this.allProspects.gains].sort(() => Math.random() - 0.5);
                const shuffledLosses = [...this.allProspects.losses].sort(() => Math.random() - 0.5);
                
                const selectedGains = shuffledGains.slice(0, 5);
                const selectedLosses = shuffledLosses.slice(0, 5);
                
                // Combine and shuffle the order of all 10 prospects
                this.prospects = [...selectedGains, ...selectedLosses].sort(() => Math.random() - 0.5);
                
                // Hide user info section and show survey
                document.getElementById('userInfoSection').style.display = 'none';
                document.getElementById('surveySection').style.display = 'block';
                
                this.showCurrentProblem();
            }
            
            calculateExpectedValue(prospect) {
                return prospect.outcomes.reduce((sum, outcome, i) => 
                    sum + outcome * prospect.probabilities[i], 0);
            }
            
            generateSureAmounts(prospect, phase = 1) {
                const [min, max] = [Math.min(...prospect.outcomes), Math.max(...prospect.outcomes)];
                const range = max - min;
                
                if (phase === 1) {
                    // Logarithmically spaced amounts
                    const amounts = [];
                    for (let i = 0; i < 7; i++) {
                        const ratio = Math.pow(10, (i / 6) * Math.log10(range + 1));
                        amounts.push(Math.round(min + ratio - 1));
                    }
                    return amounts.sort((a, b) => b - a); // Descending order
                } else {
                    // Phase 2: Linear spacing between bounds
                    const phase1Choices = this.choices[this.choices.length - 1]; // Get phase 1 choices
                    const phase1Amounts = this.generateSureAmounts(prospect, 1); // Get phase 1 amounts
                    
                    let lowestAccepted = null;
                    let highestRejected = null;
                    
                    // Find lowest accepted and highest rejected from phase 1
                    for (let i = 0; i < phase1Choices.length; i++) {
                        if (phase1Choices[i] === 'sure') {
                            // This is an accepted amount (prefer sure amount over prospect)
                            if (lowestAccepted === null || phase1Amounts[i] < lowestAccepted) {
                                lowestAccepted = phase1Amounts[i];
                            }
                        } else if (phase1Choices[i] === 'prospect') {
                            // This is a rejected amount (prefer prospect over sure amount)
                            if (highestRejected === null || phase1Amounts[i] > highestRejected) {
                                highestRejected = phase1Amounts[i];
                            }
                        }
                    }
                    
                    // Calculate bounds as specified in the paper:
                    // 25% lower than the lowest accepted value
                    // 25% higher than the highest rejected value
                    let lowerBound, upperBound;
                    
                    if (lowestAccepted !== null && highestRejected !== null) {
                        lowerBound = lowestAccepted - Math.abs(lowestAccepted) * 0.25;
                        upperBound = highestRejected + Math.abs(highestRejected) * 0.25;
                    } else if (lowestAccepted !== null) {
                        // All amounts were accepted, narrow range below lowest accepted
                        lowerBound = lowestAccepted - Math.abs(lowestAccepted) * 0.5;
                        upperBound = lowestAccepted + Math.abs(lowestAccepted) * 0.25;
                    } else if (highestRejected !== null) {
                        // All amounts were rejected, narrow range above highest rejected
                        lowerBound = highestRejected - Math.abs(highestRejected) * 0.25;
                        upperBound = highestRejected + Math.abs(highestRejected) * 0.5;
                    } else {
                        // Fallback - shouldn't happen with valid data
                        lowerBound = min;
                        upperBound = max;
                    }
                    
                    // Ensure we have the right order for descending display
                    const maxBound = Math.max(lowerBound, upperBound);
                    const minBound = Math.min(lowerBound, upperBound);
                    
                    // Generate 7 linearly spaced amounts in DESCENDING order (highest to lowest)
                    const amounts = [];
                    for (let i = 0; i < 7; i++) {
                        amounts.push(Math.round((maxBound - (i / 6) * (maxBound - minBound)) * 100) / 100);
                    }
                    return amounts;
                }
            }
            
            getDomainType(prospect) {
                return prospect.outcomes.some(outcome => outcome < 0) ? 'Loss Domain' : 'Gain Domain';
            }
            
            showCurrentProblem() {
                const prospect = this.prospects[this.currentProspectIndex];
                const expectedValue = this.calculateExpectedValue(prospect);
                const domainType = this.getDomainType(prospect);
                this.sureAmounts = this.generateSureAmounts(prospect, this.currentPhase);
                this.currentChoices = new Array(7).fill(null);
                this.errorMessage = '';
                
                // Determine the appropriate prompt text based on domain
                let promptText;
                const isLossDomain = domainType === 'Loss Domain';
                
                if (isLossDomain) {
                    promptText = "For each sure amount below, indicate whether you prefer to PAY the sure amount to not take the gamble or if you prefer to take the gamble";
                } else {
                    promptText = "For each sure amount below, indicate whether you prefer to RECEIVE the sure amount to not take the gamble or if you prefer to take the gamble";
                }
                
                const html = `
                    <div class="phase-indicator">
                        Problem ${this.currentProspectIndex + 1} of ${this.prospects.length} - Phase ${this.currentPhase}
                    </div>
                    <div class="domain-indicator">${domainType}</div>
                    
                    <div class="prospect-display">
                        <div>${prospect.description}</div>
                        <div class="expected-value">Expected Value: $${expectedValue.toFixed(2)}</div>
                    </div>
                    
                    <div id="errorMessage" class="error-message">${this.errorMessage}</div>
                    
                    <p><strong>${promptText}:</strong></p>
                    
                    <div id="choicesList">
                        ${this.sureAmounts.map((amount, index) => `
                            <div class="choice-item" id="choice${index}">
                                <div class="choice-text">
                                    Sure amount: $${amount}
                                </div>
                                <div class="choice-buttons">
                                    <button class="prefer-prospect" onclick="survey.makeChoice(${index}, 'prospect')">
                                        Prefer Gamble
                                    </button>
                                    <button class="prefer-sure" onclick="survey.makeChoice(${index}, 'sure')">
                                        Prefer Sure $${amount}
                                    </button>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                    
                    <button class="next-button" id="nextButton" onclick="survey.nextPhase()" disabled>
                        ${this.currentPhase === 1 ? 'Continue to Phase 2' : 'Next Problem'}
                    </button>
                `;
                
                document.getElementById('problemDisplay').innerHTML = html;
                this.updateProgress();
            }
            
            makeChoice(index, choice) {
                // Check for consistency errors
                const error = this.checkConsistency(index, choice);
                
                if (error) {
                    this.showError(error);
                    return;
                }
                
                this.currentChoices[index] = choice;
                
                // Update visual feedback for choice items
                const choiceElement = document.getElementById(`choice${index}`);
                choiceElement.classList.add('selected');
                choiceElement.classList.remove('error');
                
                // Update button visual feedback
                const prospectBtn = choiceElement.querySelector('.prefer-prospect');
                const sureBtn = choiceElement.querySelector('.prefer-sure');
                
                // Remove selected class from both buttons first
                prospectBtn.classList.remove('selected');
                sureBtn.classList.remove('selected');
                
                // Add selected class to chosen button
                if (choice === 'prospect') {
                    prospectBtn.classList.add('selected');
                } else {
                    sureBtn.classList.add('selected');
                }
                
                // Clear error message
                document.getElementById('errorMessage').textContent = '';
                
                // Check if all choices made
                if (this.currentChoices.every(c => c !== null)) {
                    document.getElementById('nextButton').disabled = false;
                }
            }
            
            checkConsistency(index, choice) {
                // If someone prefers a sure amount, they should prefer all higher sure amounts
                // If someone prefers the prospect, they should prefer it over all lower sure amounts
                
                if (choice === 'sure') {
                    // Check if any higher amounts were chosen as 'prospect'
                    for (let i = 0; i < index; i++) {
                        if (this.currentChoices[i] === 'prospect') {
                            return `Inconsistency: You cannot prefer the sure amount ${this.sureAmounts[index]} but reject the higher sure amount ${this.sureAmounts[i]}`;
                        }
                    }
                } else if (choice === 'prospect') {
                    // Check if any lower amounts were chosen as 'sure'
                    for (let i = index + 1; i < this.currentChoices.length; i++) {
                        if (this.currentChoices[i] === 'sure') {
                            return `Inconsistency: You cannot prefer the prospect over ${this.sureAmounts[index]} but prefer the lower sure amount ${this.sureAmounts[i]}`;
                        }
                    }
                }
                
                return null;
            }
            
            showError(message) {
                document.getElementById('errorMessage').textContent = message;
                
                // Highlight inconsistent choices
                document.querySelectorAll('.choice-item').forEach(item => {
                    item.classList.add('error');
                });
                
                // Reset choices to allow correction
                this.currentChoices = new Array(7).fill(null);
                document.querySelectorAll('.choice-item').forEach(item => {
                    item.classList.remove('selected');
                    // Also remove button selected states
                    item.querySelectorAll('button').forEach(btn => {
                        btn.classList.remove('selected');
                    });
                });
                document.getElementById('nextButton').disabled = true;
            }
            
            nextPhase() {
                if (this.currentPhase === 1) {
                    // Store phase 1 choices before moving to phase 2
                    this.choices.push([...this.currentChoices]);
                    this.currentPhase = 2;
                    this.showCurrentProblem();
                } else {
                    // Calculate certainty equivalent and move to next problem
                    this.calculateCertaintyEquivalent();
                    this.currentProspectIndex++;
                    this.currentPhase = 1;
                    
                    if (this.currentProspectIndex >= this.prospects.length) {
                        this.showResults();
                    } else {
                        this.showCurrentProblem();
                    }
                }
            }
            
            calculateCertaintyEquivalent() {
                // Find the switching point
                let lowestAccepted = null;
                let highestRejected = null;
                
                for (let i = 0; i < this.currentChoices.length; i++) {
                    if (this.currentChoices[i] === 'sure') {
                        lowestAccepted = this.sureAmounts[i];
                    } else if (this.currentChoices[i] === 'prospect' && lowestAccepted === null) {
                        highestRejected = this.sureAmounts[i];
                    }
                }
                
                let certaintyEquivalent;
                if (lowestAccepted !== null && highestRejected !== null) {
                    certaintyEquivalent = (lowestAccepted + highestRejected) / 2;
                } else if (lowestAccepted !== null) {
                    certaintyEquivalent = lowestAccepted;
                } else if (highestRejected !== null) {
                    certaintyEquivalent = highestRejected;
                } else {
                    certaintyEquivalent = 0; // No clear preference
                }
                
                const prospect = this.prospects[this.currentProspectIndex];
                const expectedValue = this.calculateExpectedValue(prospect);
                const domainType = this.getDomainType(prospect);
                
                this.results.push({
                    prospect: prospect.description,
                    expectedValue: expectedValue,
                    certaintyEquivalent: certaintyEquivalent,
                    domain: domainType,
                    riskAttitude: certaintyEquivalent < expectedValue ? 'Risk Averse' : 
                                 certaintyEquivalent > expectedValue ? 'Risk Seeking' : 'Risk Neutral'
                });
            }
            
            exportToJSON() {
                const exportData = {
                    participant: {
                        name: this.userName,
                        age: this.userAge,
                        timestamp: new Date().toISOString()
                    },
                    results: this.results,
                    summary: {
                        totalProblems: this.results.length,
                        gainProblems: this.results.filter(r => r.domain === 'Gain Domain').length,
                        lossProblems: this.results.filter(r => r.domain === 'Loss Domain').length,
                        riskAverseCount: this.results.filter(r => r.riskAttitude === 'Risk Averse').length,
                        riskSeekingCount: this.results.filter(r => r.riskAttitude === 'Risk Seeking').length,
                        riskNeutralCount: this.results.filter(r => r.riskAttitude === 'Risk Neutral').length
                    }
                };
                
                const dataStr = JSON.stringify(exportData, null, 2);
                const dataBlob = new Blob([dataStr], {type: 'application/json'});
                const url = URL.createObjectURL(dataBlob);
                const link = document.createElement('a');
                link.href = url;
                link.download = `risk_survey_${this.userName.replace(/\s+/g, '_')}_${new Date().toISOString().split('T')[0]}.json`;
                link.click();
                URL.revokeObjectURL(url);
            }
            
            exportToCSV() {
                const headers = ['Name', 'Age', 'Problem', 'Domain', 'Prospect', 'Expected_Value', 'Certainty_Equivalent', 'Risk_Attitude'];
                const rows = this.results.map((result, index) => [
                    this.userName,
                    this.userAge,
                    index + 1,
                    result.domain,
                    `"${result.prospect}"`,
                    result.expectedValue.toFixed(2),
                    result.certaintyEquivalent.toFixed(2),
                    result.riskAttitude
                ]);
                
                const csvContent = [headers, ...rows].map(row => row.join(',')).join('\n');
                const dataBlob = new Blob([csvContent], {type: 'text/csv'});
                const url = URL.createObjectURL(dataBlob);
                const link = document.createElement('a');
                link.href = url;
                link.download = `risk_survey_${this.userName.replace(/\s+/g, '_')}_${new Date().toISOString().split('T')[0]}.csv`;
                link.click();
                URL.revokeObjectURL(url);
            }
            
            showResults() {
                let html = `
                    <h2>Survey Complete - Your Results:</h2>
                    <p><strong>Participant:</strong> ${this.userName} (Age: ${this.userAge})</p>
                    <table style="width: 100%; border-collapse: collapse;">
                        <thead>
                            <tr style="background-color: #f8f9fa;">
                                <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Problem</th>
                                <th style="border: 1px solid #ddd; padding: 8px;">Domain</th>
                                <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Prospect</th>
                                <th style="border: 1px solid #ddd; padding: 8px;">Expected Value</th>
                                <th style="border: 1px solid #ddd; padding: 8px;">Your Certainty Equivalent</th>
                                <th style="border: 1px solid #ddd; padding: 8px;">Risk Attitude</th>
                            </tr>
                        </thead>
                        <tbody>
                `;
                
                this.results.forEach((result, index) => {
                    html += `
                        <tr>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">${index + 1}</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">${result.domain}</td>
                            <td style="border: 1px solid #ddd; padding: 8px;">${result.prospect}</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">${result.expectedValue.toFixed(2)}</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">${result.certaintyEquivalent.toFixed(2)}</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">${result.riskAttitude}</td>
                        </tr>
                    `;
                });
                
                const gainResults = this.results.filter(r => r.domain === 'Gain Domain');
                const lossResults = this.results.filter(r => r.domain === 'Loss Domain');
                const riskAverseCount = this.results.filter(r => r.riskAttitude === 'Risk Averse').length;
                const riskSeekingCount = this.results.filter(r => r.riskAttitude === 'Risk Seeking').length;
                const riskNeutralCount = this.results.filter(r => r.riskAttitude === 'Risk Neutral').length;
                
                html += `
                        </tbody>
                    </table>
                    
                    <h3>Summary:</h3>
                    <p><strong>Gain Domain:</strong> ${gainResults.length} problems</p>
                    <p><strong>Loss Domain:</strong> ${lossResults.length} problems</p>
                    <p><strong>Risk Attitudes:</strong></p>
                    <ul>
                        <li>Risk Averse: ${riskAverseCount} problems</li>
                        <li>Risk Seeking: ${riskSeekingCount} problems</li>
                        <li>Risk Neutral: ${riskNeutralCount} problems</li>
                    </ul>
                    
                    <div style="margin-top: 30px;">
                        <button class="export-button" onclick="survey.exportToJSON()">Export as JSON</button>
                        <button class="export-button" onclick="survey.exportToCSV()">Export as CSV</button>
                    </div>
                    
                    <p style="margin-top: 20px;"><strong>Thank you for participating in this risk preference survey!</strong></p>
                    <p>Your responses help us understand how people make decisions under risk and uncertainty.</p>
                `;
                
                document.getElementById('problemDisplay').innerHTML = '';
                document.getElementById('results').innerHTML = html;
                document.getElementById('results').style.display = 'block';
            }
            
            updateProgress() {
                const totalSteps = this.prospects.length * 2; // 2 phases per prospect
                const currentStep = this.currentProspectIndex * 2 + (this.currentPhase - 1);
                const progress = (currentStep / totalSteps) * 100;
                document.getElementById('progressBar').style.width = progress + '%';
            }
        }
        
        // Initialize the survey
        const survey = new ProspectSurvey();
    </script>
</body>
</html>
