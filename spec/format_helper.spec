require File.dirname(__FILE__) + '/spec_helper'

describe FrontendFormatHelper, "when receiving ipv4 address" do
  
  Local_IPv4_address1_to_format = IpRange.new("192.168.100.198/24")
  IPv4_address2_to_format = IpRange.new("72.98.11.7/31")
  IPv4_address3_to_format = IpRange.new("88.91.18.9/21")
  IPv4_address4_to_format = IpRange.new("212.18.13.13/32")
  IPv4_address5_to_format = IpRange.new("193.13.19.98/31")
    
  it "should return print out the correct IP-address for hash #{Local_IPv4_address1_to_format}" do 
    expected_result = {:net => "192.168.100.", :mixed => nil, :host => "198"}
    FrontendFormatHelper.new(Local_IPv4_address1_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for hash #{IPv4_address2_to_format}" do 
    expected_result = {:net => "072.098.011.", :mixed => "007", :host => nil}
    FrontendFormatHelper.new(IPv4_address2_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for hash #{IPv4_address3_to_format}" do 
    expected_result = {:net => "088.091.", :mixed => "018.", :host => "009"}
    FrontendFormatHelper.new(IPv4_address3_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for hash #{IPv4_address4_to_format}" do 
    expected_result = {:net => "212.018.013.013", :mixed => nil, :host => nil}
    FrontendFormatHelper.new(IPv4_address4_to_format).dotted_hash.should == expected_result
  end
  
  it "should return print out the correct IP-address for hash #{IPv4_address5_to_format}" do 
    expected_result = {:net => "193.013.019.", :mixed => "098", :host => nil}
    FrontendFormatHelper.new(IPv4_address5_to_format).dotted_hash.should == expected_result
  end
  
end