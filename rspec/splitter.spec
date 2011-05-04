require File.dirname(__FILE__) + '/spec_helper'

describe Splitter, "when receiving ipv4 address" do
  Local_IPv4_address_to_split1 = "192.168.0.198/24"
  IPv4_address_to_split2 = "172.16.25.1/21"
  IPv4_address_to_split3 = "7.92.23.79/8"
  IPv4_address_to_split4 = "62.18.29.1/31"
  
  it "should return the 3 net sections, 0 mixed sections and 1 host section when receiving #{Local_IPv4_address_to_split1}" do
    expected_result = {:net => ["192", "168", "000"], :mixed => [], :host => ["198"]}
    IPAddress::IPv4.new(Local_IPv4_address_to_split1).split.should == expected_result
  end
  
  it "should return the 2 net sections, 1 mixed sections and 1 host section when receiving #{IPv4_address_to_split2}" do 
    expected_result = {:net => ["172", "016"], :mixed => ["025"], :host => ["001"]}
    IPAddress::IPv4.new(IPv4_address_to_split2).split.should == expected_result
  end
  
  it "should return the 1 net sections, 0 mixed sections and 3 host section when receiving #{IPv4_address_to_split3}" do 
    expected_result = {:net => ["007"], :mixed => [], :host => ["092", "023", "079"]}
    IPAddress::IPv4.new(IPv4_address_to_split3).split.should == expected_result
  end
  
  it "should return the 3 net sections, 1 mixed sections and 0 host section when receiving #{IPv4_address_to_split4}" do 
    expected_result = {:net => ["062", "018", "029"], :mixed => ["001"], :host => []}
    IPAddress::IPv4.new(IPv4_address_to_split4).split.should == expected_result
  end
end

describe Splitter, "when receiving ipv6 address" do
  IPv6_address_to_split1 = "0:0:0:0:0:ffff:d4cc:65d2/96"
  IPv6_address_to_split2 = "2001:bf0:c000::/35"
  IPv6_address_to_split3 = "1985::/8"
  
  it "should return the 6 net sections, 0 mixed sections and 2 host section when receiving #{IPv6_address_to_split1} (IPv4 mapped IPv6 address)" do 
    expected_result = {:net => ["0000","0000","0000","0000","0000","ffff"], :mixed => [], :host => ["d4cc","65d2"]}
    IPAddress::IPv6.new(IPv6_address_to_split1).split.should == expected_result
  end
  
  it "should return the 2 net sections, 1 mixed sections and 6 host section when receiving #{IPv6_address_to_split2} (ip range of Individual Network Berlin e.V.)" do 
    expected_result = {:net => ["2001","0bf0"], :mixed => ["c"], :host => ["000","0000","0000","0000","0000","0000"]}
    IPAddress::IPv6.new(IPv6_address_to_split2).split.should == expected_result
  end
  
  it "should return the 1 net sections, 0 mixed sections and 8 host section when receiving #{IPv6_address_to_split3}" do 
    expected_result = {:net => ["19"], :mixed => [], :host => ["85","0000","0000","0000","0000","0000","0000","0000"]}
    IPAddress::IPv6.new(IPv6_address_to_split3).split.should == expected_result
  end
  
end