// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PolizeDoge is ERC20, Ownable {
    uint256 public burnRate = 2;          // 2% burn rate on each transaction
    uint256 public rewardRate = 3;        // 3% redistributed to holders
    uint256 public reportReward = 1000 * 10 ** decimals(); // Reward for reporting scams
    address public liquidityPoolAddress;  // Liquidity pool address

    mapping(address => uint256) public rewardsClaimed; // Track rewards claimed by each address
    event Burn(address indexed from, uint256 amount);
    event ScamReported(address indexed reporter, uint256 rewardAmount, string reportMessage);

    constructor() ERC20("Polize Doge", "PDOGE") Ownable(msg.sender) {
        _mint(msg.sender, 911000000 * 10 ** decimals()); // Mint initial supply of 911 million tokens
    }

    // Set the liquidity pool address
    function setLiquidityPool(address _liquidityPoolAddress) external onlyOwner {
        liquidityPoolAddress = _liquidityPoolAddress;
    }

    // Update burn and reward rates
    function setRates(uint256 _burnRate, uint256 _rewardRate) external onlyOwner {
        burnRate = _burnRate;
        rewardRate = _rewardRate;
    }

    // Set the reward amount for scam reporting
    function setReportReward(uint256 _reportReward) external onlyOwner {
        reportReward = _reportReward;
    }

    // Transfer function with burn and reward distribution
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 rewardAmount = (amount * rewardRate) / 100;
        uint256 transferAmount = amount - burnAmount - rewardAmount;

        // Burn a portion of the tokens
        _burn(msg.sender, burnAmount);
        emit Burn(msg.sender, burnAmount);

        // Transfer the remaining amount
        bool success = super.transfer(recipient, transferAmount);
        require(success, "Transfer failed");

        // Reward the sender with the reward portion for simplicity
        if (rewardAmount > 0) {
            _mint(msg.sender, rewardAmount);
        }

        return success;
    }

    // Function to reward users for reporting scams
    function reportScam(string memory reportMessage) external {
        require(bytes(reportMessage).length > 0, "Report message cannot be empty");

        // Reward the reporter with tokens if they haven't claimed too frequently
        require(rewardsClaimed[msg.sender] < reportReward, "Reward already claimed");

        _mint(msg.sender, reportReward);
        rewardsClaimed[msg.sender] += reportReward;
        emit ScamReported(msg.sender, reportReward, reportMessage);
    }
}
